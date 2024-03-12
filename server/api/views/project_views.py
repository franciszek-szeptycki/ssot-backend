from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from ..models import Project
from ..serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Project.objects.filter(owner_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Project.objects.filter(owner_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner_id=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()