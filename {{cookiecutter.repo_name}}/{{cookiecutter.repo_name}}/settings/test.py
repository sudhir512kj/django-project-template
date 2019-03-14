from settings.local import *


SEND_EMAILS = False

DATABASES['default']['TEST'] = {
    'NAME': '{{ cookiecutter.repo_name }}_test',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Use session in tests to make api login easier
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ('rest_framework.authentication.SessionAuthentication',)
