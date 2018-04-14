from django.contrib import admin

# Register your models here.
from Test.models import Test

admin.site.register([Test])
