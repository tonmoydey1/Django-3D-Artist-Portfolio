# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import BadHeaderError
from smtplib import SMTPException
import logging
from .models import Enquiry


logger = logging.getLogger(__name__)


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

        enquiry = Enquiry.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        full_message = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            messages.success(request, "Message Sent Successfully!")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        sent_count = 0

        try:
            sent_count = send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['tonmoydeyrick@gmail.com'],
                fail_silently=True
            )
        except BadHeaderError:
            messages.success(request, "Message Sent Successfully!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except (SMTPException, OSError) as exc:
            logger.warning("Contact form email failed: %s", exc)
            messages.success(request, "Message Sent Successfully!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as exc:
            logger.exception("Unexpected contact form error: %s", exc)
            messages.success(request, "Message Sent Successfully!")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if sent_count:
            enquiry.email_sent = True
            enquiry.save(update_fields=['email_sent'])

        messages.success(request, "Message Sent Successfully!")

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')
