from django.shortcuts import render,get_object_or_404
from . models import blog
# Create your views here.
def home(request):
    obj=blog.objects.all()
    return render(request,'index.html',{'data':obj})

def detail(request,id):
    obj=get_object_or_404(blog,pk=id)
    return render(request,'single-post.html',{'obj':obj})

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')