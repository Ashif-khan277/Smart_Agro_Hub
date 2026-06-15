from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-crop/', views.add_crop_view, name='add_crop'), # പുതിയ വഴി ഇതാ ഇവിടെ!
]