from rest_framework import viewsets, status
from rest_framework.response import Response

from template_core.custom_auth import SupabaseAuthentication
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    authentication_classes = [SupabaseAuthentication]
    permission_classes = [IsAuthenticated]