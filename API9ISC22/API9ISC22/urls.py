"""API9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home, About, Blog, Contact, Elements, Portfolio, Services, Single
from api import views

urlpatterns = [
  
  
 #path('admin/', admin.site.urls),
     path('', Home.as_view(),name='index.html'),
     path('about/', About.as_view(),name='about'),
     path('blog/', Blog.as_view(),name='blog'),
     path('contact/', Contact.as_view(),name='contact'),
     path('elements/', Elements.as_view(),name='elements'),
     path('portfolio/', Portfolio.as_view(),name='portfolio'),
     path('services/', Services.as_view(),name='services'),
     path('single/', Single.as_view(),name='single'),
     path('signin/', views.signin,name='signin'),
     path('signup/', views.signup,name='signup'),
     path('logout/',views.signout, name='logout'),
     path('enviar_correo/<str:correo>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
]