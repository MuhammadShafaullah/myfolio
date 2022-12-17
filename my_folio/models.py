from django.db import models
import datetime
import os
# Create your models here.

# How to Setup Images display setteing in django  


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('my_folio/static/projects_images', filename)



def filepath_posts(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('my_folio/static/Blog_images', filename)

class User_message(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    user_subject=models.CharField(max_length=200)
    user_message=models.TextField(max_length=500)
    

    
class My_projects(models.Model):
    project_name=models.CharField(max_length=100)
    project_cat=models.CharField(max_length=50,default="")
    project_clinet=models.CharField(max_length=50)
    project_date=models.DateField()
    project_url=models.URLField()
    project_details=models.TextField(max_length=500) 
    project_img1=models.ImageField(upload_to=filepath,null=True, blank=True)
    project_img2=models.ImageField(upload_to=filepath,null=True, blank=True)
    project_img3=models.ImageField(upload_to=filepath,null=True, blank=True)

    
    
class Blog_Postes(models.Model):
    Blog_name=models.CharField(max_length=100,null=True)
    Blog_cat=models.CharField(max_length=50,default="",null=True)
    Blog_date=models.DateField(null=True)
    Blog_shourtdetails=models.TextField(max_length=200,null=True)
    Blog_details=models.TextField(max_length=5000,null=True) 
    Blog_conclusion=models.TextField(max_length=700,null=True) 
    Blog_img1=models.ImageField(upload_to=filepath_posts,null=True, blank=True)  
    
class Blog_comment(models.Model):
    user=models.ForeignKey(Blog_Postes,on_delete=models.CASCADE,null=True)
    comment_date=models.DateField(auto_now_add=True, blank=True)
    user_name=models.CharField(max_length=100,null=True)
    user_email=models.EmailField(null=True)
    user_site=models.CharField(max_length=200,null=True)
    user_comment=models.TextField(max_length=500,null=True)             
       