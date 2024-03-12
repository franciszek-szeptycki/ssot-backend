from django.urls import path
from .views import *

urlpatterns = [
    path('area/', AreaListCreateAPIView.as_view(), name='area-list-create'),
    path('area/<int:pk>/', AreaDetailAPIView.as_view(), name='area-detail'),

    path('project/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),

    path('section/', SectionListCreateAPIView.as_view(), name='section-list-create'),
    path('section/<int:pk>/', SectionDetailAPIView.as_view(), name='section-detail'),

    path('quote/', QuoteListCreateAPIView.as_view(), name='quote-list-create'),
    path('quote/<int:pk>/', QuoteDetailAPIView.as_view(), name='quote-detail'),

    path('task/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]
