from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from django.views.generic import TemplateView, RedirectView


# Create your views here.
class Index(TemplateView):
    
    template_name = 'index.html'

index = Index.as_view()