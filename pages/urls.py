from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validation', views.validation, name='validation'),
    path('forecast', views.forecast, name='forecast'),
    path('models', views.models, name='models')
]
