from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, MembershipForm
from django.contrib import messages

# Create your views here.
def contact(request):

    submitted = False

    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            return HttpResponseRedirect('/contact/')
        else:
            print('Form is invalid')
    context = { 
        'form':form,
        'navbar': 'contact_page'
    }
    return render(request, 'contact.html', context)

def membership(request):

    submitted = False

    form = MembershipForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = MembershipForm(data=contact_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            return HttpResponseRedirect('/membership/')
        else:
            print('Form is invalid')
    context = { 
        'form':form,
        'navbar': 'contact_page'
    }
    return render(request, 'membership.html', context)