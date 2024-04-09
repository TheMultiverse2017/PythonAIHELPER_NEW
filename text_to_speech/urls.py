from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.texttovoiceHome,name='texttovoice.home'),
    path('texttovoice/submit/',views.texttovoiceConvert,name='texttovoice.submit'),

]