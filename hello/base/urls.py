from django.urls import path
from . import views
urlpatterns =[
     path('', views.hello,name='home'),
     path('greet', views.greet,name='greet')
]