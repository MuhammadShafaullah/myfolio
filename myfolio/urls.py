from django.contrib import admin
from django.urls import path,include


#===> How to display Images in django tempalates from db

# step 04 add hese lib t 

from django.conf import settings                    #added for image
from django.conf.urls.static import static        #added for image

#-----end

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_folio.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#   Step 05  set the condition

if settings.DEBUG:                                #added for image
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#-----