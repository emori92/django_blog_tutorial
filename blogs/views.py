from django.shortcuts import render, redirect
from django.urls import reverse
import logging

from django.views import View
from django.views.generic import TemplateView, RedirectView


# logging
logger = logging.getLogger(__name__)


# Create your views here.
class Index(TemplateView):
    template_name = 'blogs/index.html'
