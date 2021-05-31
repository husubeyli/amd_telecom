
from django.urls import reverse_lazy
from django.contrib.messages import success
from django.shortcuts import redirect
from django.views.generic.edit import (
    CreateView,
)
from .models import Contact
from .forms import ContactForm
from django.contrib.messages import success
from django.shortcuts import redirect



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy('index:home')

    def form_valid(self, form):
        success(self.request, 'Mesajınız qeydə alınmışdır tez bir zamanda sizinlə əlaqə saxlanılılacaq.')
        return super().form_valid(form)