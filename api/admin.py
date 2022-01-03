from django.contrib import admin

from api.models import Firmware, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Firmware)
