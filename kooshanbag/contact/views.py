from django.shortcuts import render, redirect
from django.views.generic import View
from .models import UserContact, Contact
from .forms import UserContactForm





class ContactUs(View):
    def get(self, request):
        contacts = Contact.objects.all()
        form = UserContactForm
        return render(request, 'contact/contact.html', {
            'contacts' : contacts,
            'form' : form
        })
        
    def post(self, request):
        form = UserContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            UserContact.objects.create(
                name = cd['name'],
                phone = cd['phone'],
                email = cd['email'],
                title = cd['title'],
                text = cd['text']
            )
            return redirect('contact:contact')
        return render(request, 'contact/contact.html', {
            'form' : form
        })
