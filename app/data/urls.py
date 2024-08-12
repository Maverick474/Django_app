from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='index'),
    path('data/', views.data, name='data'),
    path('histogram/', views.hist, name='histogram'),
    path('scatter/', views.scatter, name='scatter'),
    path('pie/', views.pie, name='pie'),
    path('box', views.box, name='box'),
    path('frequency', views.frequency, name='frequency')

]
