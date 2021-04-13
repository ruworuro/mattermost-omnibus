from .common import *

import sys
sys.setrecursionlimit(100000)

##################
# MEDIA SETTINGS #
##################

{#
DEFAULT_FILE_STORAGE = "taiga_contrib_protected.storage.ProtectedFileSystemStorage"
#}
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
MEDIA_URL = "{{ 'https' if https else 'http' }}://{{ fqdn }}/taiga/media/"
MEDIA_ROOT = "{{ taiga_back_media }}"

##################
# SITES SETTINGS #
##################

STATIC_URL = "{{ 'https' if https else 'http' }}://{{ fqdn }}/taiga/static/"
SITES["front"]["scheme"] = "{{ 'https' if https else 'http' }}"
SITES["front"]["domain"] = "{{ fqdn }}"
SITES["api"]["scheme"] = "{{ 'https' if https else 'http' }}"
SITES["api"]["domain"] = "{{ fqdn }}"

##################
# BASIC SETTINGS #
##################

{#
#SECRET_KEY = "{{ taiga_secret_key }}"

#DEBUG = {{ 'True' if debug else 'False'}}
#PUBLIC_REGISTER_ENABLED = {{ 'True' if allow_register else 'False' }}
#DEFAULT_PROJECT_SLUG_PREFIX = {{ 'True' if use_prefix_for_projects else 'False' }}
#}
DEBUG = False
PUBLIC_REGISTER_ENABLED = False
DEFAULT_PROJECT_SLUG_PREFIX = False

CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds

DEFAULT_FROM_EMAIL = "{{ email }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#########################################
## TAIGA ASYNC
#########################################
{#
{% if celery_enabled %}
CELERY_ENABLED = True
{% endif %}
#}
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100

from kombu import Queue  # noqa

# TODO Find proper variable
{#
CELERY_BROKER_URL = "amqp://taiga:{{ rabbitmq_password }}@localhost:5672/celery"
CELERY_TIMEZONE = "UTC"
#}

#########################
# TAIGA EVENTS SETTINGS #
#########################

{#
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:{{ rabbitmq_password }}@localhost:5672/taiga"}
#}

##################
# EMAIL SETTINGS #
##################
{#
{% if email_sending %}
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = {{ 'True' if email_use_tls else 'False'}}
EMAIL_HOST = "{{ email_host }}"
EMAIL_HOST_USER = "{{ email_host_user }}"
EMAIL_HOST_PASSWORD = "{{ email_host_password }}"
EMAIL_PORT = {{ email_port }}
{% endif %}
#}

###################
# SENTRY SETTINGS #
###################

{#
{% if sentry_dsn is defined %}
RAVEN_CONFIG = {
    "dsn": "{{ sentry_dsn }}",
    "timeout": 10,
}
{% endif %}

NOTIFICATIONS_CUSTOM_FILTER = {{ 'True' if notifications_custom_filter else 'False' }}
#}

################
# AUTH PLUGINS #
################
{#
{% if github_login is defined %}
GITHUB_API_CLIENT_ID = "{{ github_client_id | default("github_client_id")}}"
GITHUB_API_CLIENT_SECRET = "{{ github_secret | default("hypersecretgithubsecret") }}"
{% endif %}
{% if gitlab_login is defined %}
GITLAB_API_CLIENT_ID = "{{ gitlab_client_id | default("gitlab_client_id") }}"
GITLAB_API_CLIENT_SECRET = "{{ gitlab_api_secret | default("yourapisecret")}}"
GITLAB_URL="{{ gitlab_url | default("gitlab.example.com")}}"
{% endif %}
#################
# OTHER PLUGINS #
#################
{% if plugins is defined %}
INSTALLED_APPS += [
{% for plugin in plugins %}
    "{{ plugin.app_name }}",
{% endfor %}
]
{% endif %}
#}
