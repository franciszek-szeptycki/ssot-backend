from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    name = models.CharField(max_length=100)
    is_open = models.BooleanField()
    order = models.IntegerField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    color = models.CharField(max_length=100)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField()
    view = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    is_open = models.BooleanField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Task(models.Model):
    content = models.TextField()
    date = models.DateField(null=True, blank=True)
    duration = models.IntegerField()
    is_completed = models.BooleanField()
    is_time_set = models.BooleanField()
    priority = models.BooleanField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.IntegerField()
    completed_subtasks = models.IntegerField()
    subtasks = models.IntegerField()

    def __str__(self):
        return self.content

    def change_order(self, new_order):
        old_order = self.order
        if old_order < new_order:
            tasks = Task.objects.filter(order__gt=old_order, order__lte=new_order, section_id=self.section_id)
            for task in tasks:
                task.order -= 1
                task.save()
        else:
            tasks = Task.objects.filter(order__lt=old_order, order__gte=new_order, section_id=self.section_id)
            for task in tasks:
                task.order += 1
                task.save()
        self.order = new_order
        self.save()
