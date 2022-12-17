from django.shortcuts import render
from .models import User_message,Blog_comment,My_projects,Blog_Postes
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm,SignInForm
from datetime import date
# Create your views here.
from django.contrib.auth import authenticate,login,logout #for login

def index(request):
    form=SignUpForm() 
    formlogin=SignInForm()
    myprojects=My_projects.objects.all()
    myBlogpostes=Blog_Postes.objects.all()
    
    if request.method=='POST':
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_subject=request.POST.get('subject')
        user_message=request.POST.get('message')
        message=User_message(user_name=user_name,user_email=user_email,user_subject=user_subject,user_message=user_message)
        message.save()
        messages.success(request, 'Your massage has been sent. Thank you!')
        return render(request,'index.html',{'form':form,'formloin':formlogin,'myprojects':myprojects,'Blogposts':myBlogpostes})
   
    return render(request,'index.html',{'form':form,'formloin':formlogin,'myprojects':myprojects,'Blogposts':myBlogpostes})


def Blog(request,id):
    myBlogpostes=Blog_Postes.objects.get(id=id)
    blogcomments=Blog_comment.objects.filter(user=id)
    total_comment=len(Blog_comment.objects.filter(user=id))
    blogposts=Blog_Postes.objects.all()
    if request.method=='POST':
        blogcomments=Blog_comment.objects.filter(user=id)
        total_comment=len(Blog_comment.objects.filter(user=id))
        blogposts=Blog_Postes.objects.all()
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_site=request.POST.get('site')
        user_comment=request.POST.get('message')
        message=Blog_comment(user=myBlogpostes,comment_date=date.today(),user_name=user_name,user_email=user_email,user_site=user_site,user_comment=user_comment)
        message.save()
        # messages.success(request, 'Your massage has been sent. Thank you!')
        return render(request,'blog-single.html',{'Blogposts':myBlogpostes,'blogcomments':blogcomments,'totalcomment':total_comment,'posts':blogposts})

    return render(request,'blog-single.html',{'Blogposts':myBlogpostes,'blogcomments':blogcomments,'totalcomment':total_comment,'posts':blogposts})

def Portfolio(request,id):
    myprojects=My_projects.objects.get(id=id)
    return render(request,'portfolio-details.html',{'project':myprojects})

# SignUp using django UserCreationForm
def sign_up(request):
    form=SignUpForm()
    formlogin=SignInForm()
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            # group=Group.objects.get(name='User')
            # user.groups.add(group)
            # messages.info(request,'Signup Successfully!')
            print("Ho gaya")
            
            return render(request,'index.html',{'form':form,'formloin':formlogin})
    else:   
        return render(request,'index.html',{'form':form,'formloin':formlogin})


def sign_in(request):
    if not request.user.is_authenticated:
        formlogin=SignInForm()
        form=SignUpForm()
        if request.method == 'POST':
            fm = SignInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                print(uname)
                user=authenticate(username=uname,password=upass)
                if user is not None:
                        
                    login(request,user)
                        # messages.success(request, 'Logged in Sueccssfuly!')
                        
                    print("############Ho gaya")
                    return render(request,'index.html',{'form':form,'formloin':formlogin})
    
            else:
                return render(request,'index.html',{'form':form,'formloin':formlogin})
        else:
            return render(request,'index.html',{'form':form,'formloin':formlogin})
    else:
        return HttpResponseRedirect('/index/')    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
