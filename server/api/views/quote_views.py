from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from ..models import Quote
from ..serializers import QuoteSerializer
from rest_framework.permissions import IsAuthenticated


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Quote.objects.filter(owner_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Quote.objects.filter(owner_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner_id=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()