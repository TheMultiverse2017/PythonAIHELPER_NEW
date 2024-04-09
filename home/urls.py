from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('text_to_speech/',include('text_to_speech.urls')),
    path('storygenerator/',include('storygenerator.urls')),
    path('user/',include('user_reg_logIn.urls')),

]