# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'note', 'completed', 'created_at', 'updated_at')


admin.site.register(Todo, TodoAdmin)
admin.site.site_header = 'Todo API'
