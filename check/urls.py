from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('base/', views.base),
    path('newform/',views.satInfo),
    path('input/',views.input),
    
    
    
]