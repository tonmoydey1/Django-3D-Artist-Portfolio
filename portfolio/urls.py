# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('send-enquiry/', send_enquiry, name='send_enquiry'),
    path('about/', about, name='about'),
    path('work/', work, name='work'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', terms_conditions, name='terms_conditions'),
    path(
        'send-enquiry/',
        send_enquiry,
        name='send_enquiry'
    ),
]
