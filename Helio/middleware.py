from typing import Any
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        session = request.COOKIES.get('sessionid')

        if request.path == '/accounts/login/':
            return self.get_response(request)

        if session:
            user_id = self.verify_session(session)
            if user_id:
                request.user_id = user_id
                return self.get_response(request)

        return HttpResponseForbidden()
    
    def verify_session(self, session):
        try:
            session = Session.objects.get(session_key=session)
            user_id = session.get_decoded().get('_auth_user_id')
            return user_id
        except (ValueError, User.DoesNotExist):
            return None