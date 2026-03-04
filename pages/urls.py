from django.urls import path
from . import views

urlpatterns=[
    path('Home',views.index,name='index123'),
    path('about',views.about,name='about')
]