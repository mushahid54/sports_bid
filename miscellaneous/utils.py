from miscellaneous.mixin import EmailTemplate

__author__ = 'Mushahid Khan'

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from rest_framework import exceptions, status
from rest_framework.compat import set_rollback
from miscellaneous.paginators import CustomPagination

from rest_framework.response import Response


import os
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response
from miscellaneous.mixin import EmailTemplate
import sendgrid
from sendgrid.helpers.mail import *


def split_name(full_name):
    name_components = full_name.split(" ")

    if name_components.__len__() < 2:
        first_name, last_name = name_components[0], ""
    elif name_components.__len__() == 2:
        first_name, last_name = name_components
    else:
        last_name = name_components[-1]
        del name_components[-1]
        first_name = " ".join(name_components)

    return first_name.title(), last_name.title()

def custom_exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.

    Created by:  Mushahid 02-06-17 Friday.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        custom_status_code = 1000
        if hasattr(exc, 'code'):
            custom_status_code = exc.code
        elif hasattr(exc, 'status_code'):
            custom_status_code = exc.status_code

        if isinstance(exc.detail, (list, dict)):
            data = {
                'meta': {
                    'status': custom_status_code,
                    'message': 'Error with one or more input fields.',
                    'is_error': True
                },
                'data': exc.detail
            }
        else:
            data = {
                'meta': {
                    'status': custom_status_code,
                    'message': exc.detail,
                    'is_error': True
                },
            }
            if hasattr(exc, 'data'):
                data['data'] = exc.data

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {
            'meta': {
                'status': status.HTTP_404_NOT_FOUND,
                'message': six.text_type(msg),
                'is_error': True
            }
        }
        # data = {'detail': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {
            'meta': {
                'status': status.HTTP_403_FORBIDDEN,
                'message': six.text_type(msg),
                'is_error': True
            }
        }
        # data = {'detail': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    # Note: Unhandled exceptions will raise a 500 error.
    else:
        if settings.EXCEPTION_MASKING:
            data = {
                'meta': {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': "The following Exception occured: " + exc.__class__.__name__,
                    'is_error': True
                }
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return None

def send_bulk_email_to_set_password(user, subject_template_file="", body_template_file=""):
    recipient_email = user.email
    api_key = settings.SENDGRID_API_KEY

    first_name = user.first_name
    if len(first_name) > 3:
        first_name_part = first_name[:3].upper()
    else:
        first_name_part = first_name.upper()

    final_password = "OI"+first_name_part+str(user.id)
    user.set_password(final_password)
    user.save()

    if user.instagram_image and not user.image_url:
        profile_image = user.instagram_image
        profile_image = "https://res.cloudinary.com/summerlabel/"+profile_image
    else:
        profile_image = "https://res.cloudinary.com/summerlabel/image/upload/v1525852638/avatar_qk5lbr.png"

    if user.image_url:
        profile_image = user.image_url.url

    template_file = EmailTemplate.validate_body_template_file_for_email(body_template_file)
    context = {'email': user.email, "password": final_password, 'first_name': user.first_name, "profile_image": profile_image}
    recipient_email = "mushahidcs0054@gmail.com"


    context_as_email_content = template_file.render(context)
    context_as_subject_content = EmailTemplate.validate_body_template_file_for_email(subject_template_file).render(context)
    # if os.environ.get('DJANGO_SETTINGS_MODULE') == 'project.settings.local':
    sg = sendgrid.SendGridAPIClient(apikey=api_key)
    from_email = Email("hello@oneimpression.io")
    to_email = Email(recipient_email)
    reply_to = Email("mushahid@oneimpression.io")
    subject = context_as_subject_content
    content = Content("text/html", str(context_as_email_content))
    e_mail = Mail(from_email, subject, to_email, content)
    e_mail.reply_to = reply_to
    response = sg.client.mail.send.post(request_body=e_mail.get())

    if response.status_code == 202:
        return Response({"message": "We Will Contact You Soon..!!! "}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Failed to send message "}, status=status.HTTP_404_NOT_FOUND)
    # else:
    #     return Response({"message": "calling by staging or local "}, status=status.HTTP_200_OK)


class TalentTagPagination(CustomPagination):
    page_size = 500


class CountryPagination(CustomPagination):
    page_size = 500

class CityPagination(CustomPagination):
    page_size = 500
