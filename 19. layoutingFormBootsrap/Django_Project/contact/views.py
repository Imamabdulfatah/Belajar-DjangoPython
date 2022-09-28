from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def index(request):
    contact_form = ContactForm()
    context = {
        'heading' : 'contact',
        'data_form' : contact_form,
    }

    return render(request, 'contact/index.html', context)
