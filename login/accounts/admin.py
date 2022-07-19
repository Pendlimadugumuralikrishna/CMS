from django.contrib import admin
from .models import package
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(package)
admin.site.unregister(Group)
admin.site.site_header = "RECEIVED PACKAGES"
