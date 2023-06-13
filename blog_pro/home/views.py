from django.shortcuts import render, get_object_or_404, redirect
from . models import blog,comment
# Create your views here.
def home(request):
    obj=blog.objects.all()
    return render(request,'index.html',{'data':obj})

def detail(request,id):
    # if request.method == "POST":
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     subject=request.POST['name']
    #     message=request.POST['message']
    #     com=comment()
    #
    #     com.name = name
    #     com.email = email
    #     com.subject = subject
    #     com.message = message
    #     com.save()
    #
    # obj1=comment.objects.all()
    obj=get_object_or_404(blog,pk=id)

    return render(request,'single-post.html',{'obj':obj})


def comm(request):
    comments = request.POST.get('comment')
    comid = request.POST.get('comid')
    #userid= request.session['userid']

    news=blog.objects.get(id=comid)


    tbl = comment(comments=comments, news=newsh)
    tbl.save()
    return redirect(detail,id=comid)


def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')

