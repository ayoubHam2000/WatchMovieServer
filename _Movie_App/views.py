from django.db.models.fields.files import ImageField
from django.shortcuts import render
from django.http.response import HttpResponse

from .models import (
    MovieModel
)

import json


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
    dic = {}
    dic["name"] = "movie1"
    dic["pathimage"] = "http://192.168.0.65:8000/static/media/images/movies/Capture%20d%E2%80%99%C3%A9cran%20(1).png"
    if (request.POST) :
        newobg = MovieModel()
        newobg.name = request.POST.get('name')
        newobg.studio = request.POST.get('studio')
        newobg.movieImage = ImageField()
        newobg.save()
    return HttpResponse(json.dumps(dic))