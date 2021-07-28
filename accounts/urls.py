from accounts.views import signupView
from django.urls import path
from .views import signupView , loginView ,logoutView

app_name = 'accounts'

urlpatterns = [
path('signup/',signupView,name='signupView'),
path('login/',loginView,name='loginView'),
path('logout/',logoutView,name='logoutView')

]