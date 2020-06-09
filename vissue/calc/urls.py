from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="home.html"),
    path("ab",views.result,name="result.html"),

    
]