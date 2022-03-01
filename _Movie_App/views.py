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
    if (request.POST) :
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print(f'{username}  {password}')
    return HttpResponse("Yes")
