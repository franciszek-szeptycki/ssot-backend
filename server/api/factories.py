import factory
from .models import Area, Project, Section, Quote, Task
from django.contrib.auth.models import User


def get_random_user():
    return User.objects.order_by('?').first()


class AreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Area

    name = factory.Faker('sentence')
    is_open = factory.Faker('boolean')
    order = factory.Sequence(lambda n: n)
    owner_id = factory.LazyFunction(get_random_user)


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker('sentence')
    is_active = factory.Faker('boolean')
    color = factory.Faker('color_name')
    owner_id = factory.LazyFunction(get_random_user)
    area_id = factory.SubFactory(AreaFactory)
    order = factory.Sequence(lambda n: n)
    view = factory.Faker('word')


class SectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Section

    name = factory.Faker('sentence')
    order = factory.Sequence(lambda n: n)
    is_open = factory.Faker('boolean')
    project_id = factory.SubFactory(ProjectFactory)
    owner_id = factory.LazyFunction(get_random_user)


class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quote

    author = factory.Faker('name')
    content = factory.Faker('text')
    owner_id = factory.LazyFunction(get_random_user)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    content = factory.Faker('text')
    date = factory.Faker('date_object')
    duration = factory.Faker('random_int', min=1, max=10)
    is_completed = factory.Faker('boolean')
    is_time_set = factory.Faker('boolean')
    priority = factory.Faker('boolean')
    project_id = factory.SubFactory(ProjectFactory)
    section_id = factory.SubFactory(SectionFactory)
    owner_id = factory.LazyFunction(get_random_user)
    order = factory.Sequence(lambda n: n)
    completed_subtasks = factory.Faker('random_int', min=0, max=5)
    subtasks = factory.Faker('random_int', min=0, max=10)
