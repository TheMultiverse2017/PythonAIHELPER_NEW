from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('texttovoice',views.texttovoiceHome,name='texttovoice.home'),
    path('texttovoice/submit/',views.texttovoiceConvert,name='texttovoice.submit'),
]