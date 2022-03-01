from django.urls import path

from .views import (
    test
)

app_name = "_Movie_App"

urlpatterns = [
    path('user', test, name = 'test'),
]