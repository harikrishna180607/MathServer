
from django.contrib import admin
from django.urls import path
from mathsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.calculate_bmi,
         name="BMI_calculator_root"),
    path('',views.calculate_bmi,name='home'),
]
