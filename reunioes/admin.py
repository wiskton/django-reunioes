# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Reuniao

class ReuniaoAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'data', )
    search_fields = ('assunto', 'data', )
    list_filter = ['data', ]
    filter_horizontal = ['emails', ]
    save_on_top = True
    list_per_page = 20

admin.site.register(Reuniao, ReuniaoAdmin)
