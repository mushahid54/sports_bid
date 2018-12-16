import os
from django.http import HttpResponseRedirect

__author__ = 'Mushahid_Khan'


def redirect_view(request):
    """
        Redirect based on the request path
    :param request:
    :return:
    """
    if os.environ.get('DJANGO_SETTINGS_MODULE') == 'project.settings.developer_specific':
        redirect_uri = 'https://api.example.in/admin/'   # Production URL
    else:
        redirect_uri = 'http://127.0.0.1:8000/admin/'
    return HttpResponseRedirect(redirect_uri)