# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=64, blank=False)
    note = models.TextField(max_length=320, null=True)
    completed = models.BooleanField(default=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
