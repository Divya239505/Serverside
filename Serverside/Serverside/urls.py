from django.contrib import admin
from django.urls import path
from bmiappimport views
urlspatterns =[
    path('admin/',admin.site.urls),
    path('calculatedbmi/',views.calculate_bmi,name="calculatedbmi"),
    path('',views.calculate_bmi,name="calculatedbmiroot")
]