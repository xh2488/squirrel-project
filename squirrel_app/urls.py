from django.urls import path


from . import views

urlpatterns = [path("map" , views.map),
               path("sightings", views.sighting),
               #path(r'sightings/(?P<id>[\w-]+)', views.sighting_individual),
               path("sightings/<str:squirrel_id>", views.sighting_individual),
               ]
