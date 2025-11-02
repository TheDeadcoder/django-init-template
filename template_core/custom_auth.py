from rest_framework import authentication
from rest_framework import exceptions
from .supabase_client import supabase
from rest_framework import authentication, exceptions

class SupabaseUser:
    def __init__(self, supabase_user):
        self.id = supabase_user.id
        self.email = supabase_user.email
        self.is_authenticated = True
        self.is_active = True

    @property
    def is_anonymous(self):
        return False

class SupabaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header:
            return None
        
        print("In supabase auth", auth_header)

        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        else:
            token = auth_header

        try:
            user = supabase.auth.get_user(token)
            return (SupabaseUser(user.user), None)
        except Exception as e:
            raise exceptions.AuthenticationFailed('Invalid token')

    def authenticate_header(self, request):
        return 'Bearer'