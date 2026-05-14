# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import BadHeaderError


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

        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            messages.error(request, "Email is not configured yet. Please contact me directly.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['tonmoydeyrick@gmail.com'],
                fail_silently=False
            )
        except BadHeaderError:
            messages.error(request, "Invalid message header. Please try again.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        messages.success(request, "Message Sent Successfully!")

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('/')
