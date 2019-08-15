from django.contrib import admin
from .models import GetAnimal, Organization, Executive, Manager, Employee


# Register your models here.
admin.site.register(GetAnimal)
admin.site.register(Organization)
admin.site.register(Executive)
admin.site.register(Manager)
admin.site.register(Employee)
