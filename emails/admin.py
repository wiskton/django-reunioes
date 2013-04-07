# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    save_on_top = True
    list_per_page = 20

admin.site.register(Email, EmailAdmin)
