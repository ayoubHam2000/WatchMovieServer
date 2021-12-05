from django.urls import path

from .views import (
    test
)

app_name = "_Movie_App"

urlpatterns = [
    path('', test, name = 'test'),
]