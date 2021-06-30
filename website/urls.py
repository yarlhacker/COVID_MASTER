from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index, name='index' ),
    path('about/' , views.about , name='about' ),
    path('doctors' , views.doctors, name='doctors' ),
    path('news' , views.news, name='news' ),
    path('protect' , views.protect, name='protect' ),
   

]