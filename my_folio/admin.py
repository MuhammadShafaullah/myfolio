from django.contrib import admin
from .models import User_message,Blog_comment,My_projects,Blog_Postes
# Register your models here.


@admin.register(User_message)
class User_message(admin.ModelAdmin):
    list_display=('id','user_name','user_email','user_subject','user_message')

@admin.register(Blog_comment)
class Blog_comment(admin.ModelAdmin):
    list_display=('id','comment_date','user_name','user_email','user_site','user_comment')
    
@admin.register(My_projects)
class My_projects(admin.ModelAdmin):
    list_display=('id','project_name','project_cat','project_clinet','project_date','project_url','project_details','project_img1','project_img2','project_img3')    
    
@admin.register(Blog_Postes)
class Blog_Postes(admin.ModelAdmin):
    list_display=('id','Blog_name','Blog_cat','Blog_date','Blog_shourtdetails','Blog_details','Blog_img1','Blog_conclusion')        
