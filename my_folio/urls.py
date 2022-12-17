from django.contrib import admin
from django.urls import path
from .import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('blog-single/<int:id>/',views.Blog,name='blog'),
    path('postcomment/<int:id>/',views.Blog,name='postcomment'),
    path('portfolio-details/<int:id>/',views.Portfolio,name='portfolio'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='sigin'),
    path('logout/',views.user_logout,name='logout'),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]