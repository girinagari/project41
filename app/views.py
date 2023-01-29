from django.shortcuts import render

# Create your views here.
def Toasts(request):
    return render(request,'Toasts.html')