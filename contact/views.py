from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .form import ContactForm
# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contacts' : contacts})

def contact_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/view.html', { 'contact' : contact})

def contact_new(request):
    form = ContactForm()
    return render(request, 'contact/new.html', {'form' : form})