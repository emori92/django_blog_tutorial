from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
]