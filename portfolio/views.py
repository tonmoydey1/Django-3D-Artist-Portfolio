# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import logging
from .models import Enquiry
from urllib import parse, request as urlrequest
from urllib.error import URLError


logger = logging.getLogger(__name__)


def send_web3forms_enquiry(name, email, subject, message):
    if not settings.WEB3FORMS_ACCESS_KEY:
        return False

    payload = parse.urlencode({
        'access_key': settings.WEB3FORMS_ACCESS_KEY,
        'name': name,
        'email': email,
        'subject': subject or 'New portfolio enquiry',
        'message': message,
        'from_name': 'Tonmoy 3D Artist Portfolio',
    }).encode()

    req = urlrequest.Request(
        'https://api.web3forms.com/submit',
        data=payload,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        method='POST',
    )

    try:
        with urlrequest.urlopen(req, timeout=8) as response:
            return 200 <= response.status < 300
    except URLError as exc:
        logger.warning("Web3Forms delivery failed: %s", exc)
        return False


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

        if send_web3forms_enquiry(name, email, subject, message):
            enquiry.email_sent = True
            enquiry.save(update_fields=['email_sent'])

        messages.success(request, "Message Sent Successfully!")

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')
