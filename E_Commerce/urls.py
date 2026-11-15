from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  

from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('register/',registerpage),
    path('login/',loginpage),
    path('logout/',logoutpage),
    path('men/',menpage),
    path('women/',womenpage),
    path('accessories/',accessoriepage),
    path('collections/',collectionpage),
    path('cart/<int:pk>/',cartpage),
    path('addtocart/<int:pk>/',addtocartpage),
    path('deletecart/<int:pk>/',deletecart),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)