from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from ..models import Section
from ..serializers import SectionSerializer
from rest_framework.permissions import IsAuthenticated


class SectionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Section.objects.filter(owner_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


class SectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Section.objects.filter(owner_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner_id=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()