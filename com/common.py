from django.conf import settings


def add_login(response, username):
    response.set_cookie(settings.SESSION_COOKIE_NAME,
                        username, max_age=settings.SESSION_COOKIE_AGE,
                        expires=None, domain=settings.SESSION_COOKIE_DOMAIN,
                        path=settings.SESSION_COOKIE_PATH,
                        secure=settings.SESSION_COOKIE_SECURE or None,
                        httponly=False)