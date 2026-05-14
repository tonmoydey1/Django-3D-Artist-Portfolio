# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def work(request):

    return render(request, 'portfolio/work.html')

def services(request):

    return render(request, 'portfolio/services.html')


def contact(request):
    
    return render(request, 'portfolio/contact.html')

def privacy_policy(request):

    return render(request, 'portfolio/privacy_policy.html')

def terms_conditions(request):

    return render(request, 'portfolio/terms_conditions.html')


def send_enquiry(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['tonmoydeyrick@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Message Sent Successfully!")

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('/')
