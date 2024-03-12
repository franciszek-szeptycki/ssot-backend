from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    authentication = JWTAuthentication()
    user, _ = authentication.authenticate(request)

    return Response({
        'username': user.username,
        'email': user.email,
    })