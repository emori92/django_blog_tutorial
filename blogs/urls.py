from django.urls import path
from .views import Index, InquiryView, BlogListView


app_name = 'blogs'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
]