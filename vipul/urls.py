from  django.urls import path
from . import views

urlpatterns = [
  path('',views.priyank,name='priyank'),
  path('add',views.add,name='add'),
  path('sub',views.sub,name='sub'),
  path('mul',views.mul,name='mul'),
  path('div',views.div,name='div')
]

