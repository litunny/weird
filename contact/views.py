from django.shortcuts import render,get_object_or_404, redirect
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
    
    if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.first_name = request.POST['first_name']
                contact.middle_name = request.POST['middle_name']
                contact.last_name = request.POST['last_name']
                contact.phone_number = request.POST['phone_number']
                contact.active = True
                contact.save()
                return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/new.html', {'form' : form})

def contact_edit (request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
            form = ContactForm(request.POST, instance=contact)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.first_name = request.POST['first_name']
                contact.middle_name = request.POST['middle_name']
                contact.last_name = request.POST['last_name']
                contact.phone_number = request.POST['phone_number']
                contact.active = True
                contact.save()
                return redirect('index')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact/edit.html', {'form' : form, 'contact' : contact})