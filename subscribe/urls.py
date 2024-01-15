from django.urls import path, include
from . import views



urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thankyou, name='thank_you' )
]
