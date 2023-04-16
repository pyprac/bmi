from django.urls import path 
from bmi_app.views import home,bmi_result
 
urlpatterns = [
path('',home,name='home'),
path('result/',bmi_result,name='bmi_result'),
]