from importlib.resources import contents
from webbrowser import get
from django.shortcuts import render,redirect
from django.template import context 
from .models import *
from .forms import *
from  django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required






# def register(request):

#     form = registerform()
#     if request.method =="Post":
#         form = registerform(request.Post)
#         if form.is_valid():
#             form.save
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'account created for {username} you can login now !')
#     context={'form':form}
#     return render(request,'app/register.html',context)


#home_page

def home(request):
    context={}
    return render(request,'beatup/home.htm',context)





#login_page

def loginpage(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            customer.user = request.user
            login(request,user)
            return redirect ('home')
    context={}
    return render(request,'beatup/login.htm',context)   



#logout_page

def logoutpage(request):
    logout(request)

    return redirect('home')

    
#community/posts_page

@login_required
def postpage (request):
    posts = Post.objects.all().order_by('-date')
     
    
    context={'posts':posts}

    return render(request,'beatup/community.htm',context)




#ADD_post_page
@login_required
def addpost(request):
    form = postform()

    if request.method=="POST":

        form= postform(request.POST)
      
        if form.is_valid():

            instance = form.save(commit=False)       
            instance.author = request.user


          
            instance.save()

            # form.save()
            # Post.objects.create(Author=request.user,text=content,date=timezone.now)
            return redirect('community')
        
    context={'form':form}
    return render(request,'beatup/addpost.htm',context) 


#EDIT_selected_post
@login_required
def edit_post(request,pk):
    post  = Post.objects.get(id=pk)
    form = postform(instance=post)
    if request.method=="POST":
        form = postform(request.POST,instance=post)
        print("flag")
        if form.is_valid():
            print("flag1")

            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            print("flag2")
            return redirect('community')

    context ={'form':form}
    return render(request,'beatup/editpost.htm',context)        




#delete_specific_post
@login_required
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method=="POST":
        post.delete()
        return redirect('community')
    
    context={'post':post}
    return render(request,'beatup/deletepost.htm',context)


#------------------------------------------------------------------


@login_required
def user_profile(request,pk):
    get_customer= customer.objects.get(id=pk)
    print(get_customer)
    get_user=get_customer.user
    print(get_user)
    get_post=Post.objects.filter(author=get_user).order_by("-date") 
    context ={'posts':get_post,'customer':get_customer}
    return render(request,'beatup/user_profile.htm',context)
