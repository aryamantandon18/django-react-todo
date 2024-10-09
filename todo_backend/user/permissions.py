from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsAuthenticatedUser(BasePermission):
    """
    Custom permission to check if the user is authenticated using JWT.
    """
    def has_permission(self, request, view):
        jwt_authenticator = JWTAuthentication()

        # Attempt to authenticate the user using the provided token
        try:
            # Authenticate returns None if authentication fails
            authenticated_user = jwt_authenticator.authenticate(request)
            
            if authenticated_user is not None:
                user, token = authenticated_user  # Unpack only if not None
                request.user = user  # Set user in request object
                return True
            else:
                raise AuthenticationFailed({"error": "Invalid token or no token provided."})
        except AuthenticationFailed:
            raise AuthenticationFailed({"error": "User is not authenticated."})

        return False
