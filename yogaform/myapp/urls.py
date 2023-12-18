from django.urls import path
from myapp import views

urlpatterns=[
    path('', views.yogaform,name='yogaform'), 
    path('update', views.updateform,name='updateform'), 
    path('completePayment',views.completePayment,name='completepayment')
]