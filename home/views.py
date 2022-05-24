from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
def em(request):
    return render(request,'em.html')
def hme(request):
    return render(request,'hme.html')
def lcd(request):
    return render(request,'lcd.html')
def stepper(request):
    return render(request,'stepper.html')
def ultra(request):
    return render(request,"ultra.html")