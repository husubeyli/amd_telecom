
from django.urls import reverse_lazy
from django.contrib.messages import success
from django.shortcuts import redirect
from django.views.generic.edit import (
    CreateView,
)
from .models import Contact
from .forms import ContactForm



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"

    def form_valid(self, form):
        success(self.request, 'Mesajiniz qeyde alinmisdir tez bir zamanda sizinle elaqe saxlanilicaq.')
        # success_url = reverse_lazy('index:home')
        return redirect('index:home')