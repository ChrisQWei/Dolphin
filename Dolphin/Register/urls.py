from django.urls import path
from Register.views import *
app_name = 'Register'

urlpatterns = [
    path('', home, name='home'),
path('add', add, name='add'),

]
