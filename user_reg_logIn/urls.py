from django.urls import path
from . import views

urlpatterns = [
    path('login/index',views.loginIndex,name='login.index'),
    path('login/submit',views.loginSubmit,name='login.submit'),
    path('register/index/',views.regIndex,name='register.index'),
    path('register/submit/',views.regSubmit,name='register.submit'),
]