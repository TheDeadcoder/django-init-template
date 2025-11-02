from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .supabase_client import supabase
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'password'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
    ),
    responses={
        200: openapi.Response('Successful Login', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
            }
        )),
        400: 'Bad Request'
    }
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'error': 'You must provide both an email and a password'}, status=400)
    
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return Response({'token': response.session.access_token})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        logger.info(f"Auth header: {auth_header}")

        if not auth_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=400)

        token = auth_header.split(' ', 1)[1] if ' ' in auth_header else auth_header
        if not token:
            return JsonResponse({'error': 'Token missing in Authorization header'}, status=400) 
        try:
            response = supabase.auth.sign_out()
            print("Supabase sign_out response:", response)
        except Exception as e:
            logger.warning(f"Supabase sign_out warning: {str(e)}")
        return JsonResponse({'message': 'Logged out successfully'})
    except Exception as e:
        logger.error(f"Error in logout view: {str(e)}", exc_info=True)
        return JsonResponse({'error': str(e)}, status=400)