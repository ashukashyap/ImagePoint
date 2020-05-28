from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [

    path('', views.home , name="Home"),
    path('category/<int:cid>/', views.show_category, name="show_Category"),
    path('search', views.search, name="Search"),
]
