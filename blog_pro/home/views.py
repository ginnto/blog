from django.shortcuts import render
from . models import blog
# Create your views here.
def home(request):
    obj=blog.objects.all()
    return render(request,'index.html',{'data':obj})

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')