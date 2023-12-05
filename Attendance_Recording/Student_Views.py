from django.shortcuts import render, redirect

def HOME(request):
    return render(request,'student/home.html')