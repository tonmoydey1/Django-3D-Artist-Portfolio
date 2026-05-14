from django.conf import settings


def web3forms_access_key(request):
    return {
        'web3forms_access_key': settings.WEB3FORMS_ACCESS_KEY,
    }
