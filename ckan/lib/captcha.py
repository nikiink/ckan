# encoding: utf-8

from ckan.common import config

import requests


def check_recaptcha(request):
    '''Check a user\'s recaptcha submission is valid, and raise CaptchaError
    on failure.'''
    recaptcha_private_key = config.get_value('ckan.recaptcha.privatekey')
    if not recaptcha_private_key:
        # Recaptcha not enabled
        return

    client_ip_address = request.environ.get(
        'REMOTE_ADDR', 'Unknown IP Address')

    # reCAPTCHA v2
    recaptcha_response_field = request.form.get('g-recaptcha-response', '')
    recaptcha_server_name = 'https://www.google.com/recaptcha/api/siteverify'

    # recaptcha_response_field will be unicode if there are foreign chars in
    # the user input. So we need to encode it as utf8 before urlencoding or
    # we get an exception (#1431).
    params = dict(
        secret=recaptcha_private_key,
        remoteip=client_ip_address,
        response=recaptcha_response_field.encode('utf8')
    )
    response = requests.get(recaptcha_server_name, params)
    data = response.json()

    try:
        if not data['success']:
            raise CaptchaError()
    except IndexError:
        # Something weird with recaptcha response
        raise CaptchaError()


class CaptchaError(ValueError):
    pass
