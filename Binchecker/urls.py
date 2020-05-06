from django.urls import path
from .views import binchecker, binform

urlpatterns = [
    path('', binform),
    path('input/', binchecker),

]