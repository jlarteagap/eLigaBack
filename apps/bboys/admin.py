from django.contrib import admin

from apps.bboys.models import Bboy, Crew, City
# Register your models here.
admin.site.register(Bboy)
admin.site.register(Crew)
admin.site.register(City)