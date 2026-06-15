from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name='home'), 
    # home page-ne views.py-ile home function-umayi connect cheyyunnu
]
