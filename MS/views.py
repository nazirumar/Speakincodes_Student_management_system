
from base64 import urlsafe_b64decode
from email import message
from msilib.schema import ListView
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout

from MS.models import Pincode, SignupForm
from .urls import  *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage 
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site  

@login_required
def index(request):
    return render(request,    'index.html')

def success(request):
    return render(request,    'accounts/confirm_success.html')

def login(request):

    return render(request,  'login.html')


def register(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active =False
            user.save()

            current_site = get_current_site(request)  
            mail_subject ='Activation link has been sent to your email id'
            message =render_to_string('accounts/acc_active_email.html',{
               'user':user,
               'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),})
            email = form.cleaned_data.get('email')
            email =EmailMessage(
            mail_subject, message,
            from_email=settings.EMAIL_FROM_USER,
             to = [user.email]
        )
            email.send()
            return redirect('success') 
    else:
        form = SignupForm()  
    return render(request, 'register.html', {'form': form})
def login(request):
        forms = SignupForm()
        if forms is not None:
            if forms.is_active:
                login(request, forms)
                return redirect('MS:UG_update')
            else:
                    return HttpResponse('Disabled account')
        else:
            form =SignupForm()
        return render(request, 'accounts/login.html', {'form': form})


def activate(request, uidb64, token):
    User = User()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user =None
    if user is not None and account_activation_token.check_token(user.token):
        user.is_email_verified =True
        user.save() 
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else: 
        return HttpResponse('Activation link is invalid')

def e_activation(request):
    if request.method=='POST':
        form = PincodeForm(request.POST)
        if '1wh7e782uwji983d' in form:
            if form.is_valid():
                form.save()
    form =PincodeForm
    context={
        'form':form
    }
    return render(request,    'accounts/Card_Activation.html', context)

def ug_Update(request):
    if request.method=='POST':
        forms= O_LEVEL(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('UG_update')
    
    dataset= O_Level.objects.all()
    forms = O_LEVEL()
    
    context={
        'forms':forms,
        'dataset':dataset
    }
    return render(request,    'ug_update.html', context)

def delete(request, pk, template_name='UG_update.html'):
    contact = get_object_or_404(O_Level, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/UG_update/')
    return render(request, template_name, {'object':contact})

def biodateupdate(request):
    if request.method=='POST':
      
        form = BioUpdateForms(request.POST)        
        if form.is_valid():
            form.save()
            users =BioUpdate.objects.all()
            request.user.new_spending.add(form)  
            return render(request,'Biodata_update.html',  {        
                'users': users
                })
        return redirect('UG_update')
    else:
        BioModel=BioUpdate.objects.all()
        form =  BioUpdateForms()
        context={
            'biomodel':BioModel,
            'form':form
        }
        return render(request,    'Biodata_update.html', context)