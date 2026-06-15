from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # നമ്മൾ എഴുതിയ register_view ഫങ്ഷൻ എടുക്കാൻ വേണ്ടി views ഇമ്പോർട്ട് ചെയ്യുന്നു

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),# http://127.0.0.1:8000/accounts/register/ എന്ന വഴി ഉണ്ടാക്കുന്നു
]
