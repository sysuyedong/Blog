from django.contrib import admin
from mysite.models import *

admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Tag)