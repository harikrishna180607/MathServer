
from django.shortcuts import render 
def calculate_bmi(request): 
    context={} 
    context['bmi'] = "" 
    context['h'] = "" 
    context['w'] = "" 
    if request.method == 'POST': 
        print("POST method is used")
        h = float(request.POST.get('Height',''))
        w = float(request.POST.get('Weight',''))
        print('request=',request) 
        print('Height=',h) 
        print('Weight=',w) 
        bmi = w / ((h / 100) ** 2)
        context['bmi'] = bmi 
        context['Weight'] = w
        context['Height'] = h 
        print('bmi=',bmi) 
    return render(request,'mathsapp/server.html',context)