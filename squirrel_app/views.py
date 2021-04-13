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








