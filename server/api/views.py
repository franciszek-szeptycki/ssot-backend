from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Area
from .serializers import AreaSerializer
from rest_framework.permissions import IsAuthenticated


class AreaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Area.objects.filter(owner_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


class AreaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Area.objects.filter(owner_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner_id=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
