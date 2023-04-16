from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'bmi_app/home.html',{})
    

def bmi_result(request):
    height=float(request.POST.get('height', False))/100 #centimeter to meter 
    weight=float(request.POST.get('weight', False))
    BMI = weight/(height*height)
    bmi = int(BMI)
    height = 'Your Height = ' + str(height) + 'm' 
    weight = 'Your Weight = ' + str(weight) + 'kg' 
    BMI = f'Your BMI = {BMI:.2f}' 
    
    if bmi<=18.5:
        level = 'You are Under weight'
    elif bmi>=18.5 and bmi<=24.9:
        level = 'You are Normal weight'
    elif bmi>25 and bmi<30:
        level = 'You have Over weight'
    else: # bmi>=30:
        level = 'You have Obesity'
   
    return render(request,'bmi_app/bmi_result.html',{'height':height,'weight':weight,'BMI':BMI,'level':level})