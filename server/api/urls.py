from django.urls import path
from .views import AreaListCreateAPIView, AreaDetailAPIView

urlpatterns = [
    path('area/', AreaListCreateAPIView.as_view(), name='area-list-create'),
    path('area/<int:pk>/', AreaDetailAPIView.as_view(), name='area-detail'),
]
