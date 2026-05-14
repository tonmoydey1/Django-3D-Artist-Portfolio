# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import logging
from .models import Enquiry
from urllib import parse, request as urlrequest
from urllib.error import HTTPError, URLError


logger = logging.getLogger(__name__)


def send_web3forms_enquiry(name, email, subject, message):
    if not settings.WEB3FORMS_ACCESS_KEY:
        logger.warning("Web3Forms access key is missing.")
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
            response_body = response.read().decode('utf-8', errors='replace')
            logger.info("Web3Forms response status=%s body=%s", response.status, response_body)
            return 200 <= response.status < 300 and '"success":true' in response_body.lower()
    except HTTPError as exc:
        error_body = exc.read().decode('utf-8', errors='replace')
        logger.warning("Web3Forms rejected enquiry: status=%s body=%s", exc.code, error_body)
        return False
    except URLError as exc:
        logger.warning("Web3Forms delivery failed: %s", exc)
        return False
    except Exception as exc:
        logger.exception("Unexpected Web3Forms delivery error: %s", exc)
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
