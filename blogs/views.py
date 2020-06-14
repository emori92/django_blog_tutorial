from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
import logging
from django.contrib import messages

from django.views import View
from django.views.generic import TemplateView, RedirectView, FormView
from .forms import InquiryForm


# logging
logger = logging.getLogger(__name__)


# Create your views here.
class Index(TemplateView):
    template_name = 'blogs/index.html'


class InquiryView(FormView):
    template_name = 'blogs/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('blogs:inquiry')
    
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info(f'Inquiry sent by {form.cleaned_data["name"]}')
        return super().form_valid(form)