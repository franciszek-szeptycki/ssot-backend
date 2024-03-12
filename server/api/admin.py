from django.contrib import admin
from .models import *

admin.site.register([Area, Project, Section, Quote, Task])