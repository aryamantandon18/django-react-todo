from user.models import User
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self,req):
        token = req.
    
            