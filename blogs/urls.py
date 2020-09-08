from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('blog_list/', views.BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]