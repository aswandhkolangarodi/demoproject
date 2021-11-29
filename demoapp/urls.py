
from django.urls import path,include
from. import views

urlpatterns = [
   path('',views.testfun,name='hello'),
   path('sample',views.fnsample,name='sample')

]
