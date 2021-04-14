from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from squirrel_app.models import squirrel_info
from squirrel_app.models import AddSquirrelForm
from django.shortcuts import get_object_or_404
import pandas as pd

def map(request):
    location_list = list(squirrel_info.objects.values("Longtitude","Latitude"))[:100]
    return render(request,'squirrel_app/map.html',{"sightings":location_list})
# Create your views here.



def sighting(request):
    squirrel_list = list(squirrel_info.objects.values("Unique_Squirrel_ID","Date"))

    return render(request,'squirrel_app/sighting.html',{"squirrel_list":squirrel_list})



def sighting_individual(request,squirrel_id):
    squirrel = squirrel_info.objects.get(Unique_Squirrel_ID=squirrel_id)
    print(squirrel)
    return render(request, 'squirrel_app/sighting_individual.html', {"squirrel": squirrel})

def add_squirrel(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddSquirrelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            print("new squirrel added")
            return HttpResponse("Thank you! Squirrel Added!")

    else:
        form = AddSquirrelForm()

    return render(request, 'squirrel_app/add.html', {'form': form})

def squirrel_stats(request):
    squirrel_list = list(squirrel_info.objects.values("Hectare_squirrel_number", "Primary_fur_color","Shift","Age","Location"))
    df = pd.DataFrame(squirrel_list)

    # Analysis on hectare squirrel number
    avg_hectare_squirrel_number = df["Hectare_squirrel_number"].mean()
    avg_hectare_squirrel_number = round(avg_hectare_squirrel_number, 4)

    # Analysis on main color
    main_color_df = df.groupby('Primary_fur_color').count()
    main_color = main_color_df['Age'].idxmax()
    main_color = str(main_color)

    # analysis on shift
    shift_df = df.groupby('Shift').count()
    am_count = shift_df.iloc[0,0]
    pm_count = shift_df.iloc[1,0]
    percent_AM = am_count/(am_count+pm_count) *100
    percent_AM = round(percent_AM,2)

    # Analysis on age
    age_df = df.groupby('Age').count()
    adult_count = age_df.iloc[1, 0]
    juv_count = age_df.iloc[2, 0]
    percent_adult = adult_count / (adult_count + juv_count) * 100
    percent_adult = round(percent_adult,2)

    # Analysis on location
    location_df = df.groupby('Location').count()
    above_count = location_df.iloc[0, 0]
    ground_plane_count = location_df.iloc[1, 0]
    percent_above = above_count / (above_count + ground_plane_count) * 100
    percent_above = round(percent_above,2)

    return render(request, 'squirrel_app/squirrel_stats.html', {"avg_hectare_squirrel_number": avg_hectare_squirrel_number, "main_color": main_color, "percent_AM": percent_AM, "percent_adult": percent_adult, "percent_above": percent_above})







