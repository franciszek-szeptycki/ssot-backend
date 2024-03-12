from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from ..models import Task
from ..serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(owner_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(owner_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner_id=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()