from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.storygenerator,name='storygenerator.home'),
    path('storygenerator/submit',views.generateStory,name='storygenerator.submit'),

]