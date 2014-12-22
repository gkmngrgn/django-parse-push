from django.conf import settings

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")
APPLICATION_ID = getattr(settings, "PARSE_APPLICATION_ID", "")
REST_API_KEY = getattr(settings, "PARSE_REST_API_KEY", "")
