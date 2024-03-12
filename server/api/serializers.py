from rest_framework import serializers
from .models import *


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'is_open', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'is_active', 'color', 'owner_id', 'area_id', 'order', 'view']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'order', 'is_open', 'project_id']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'author', 'content', 'owner_id']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'content', 'date', 'duration', 'is_completed', 'is_time_set', 'priority', 'project_id',
                  'section_id', 'owner_id', 'order', 'completed_subtasks', 'subtasks']
