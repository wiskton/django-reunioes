# -*- coding: utf-8 -*-
from django.db import models
from emails.models import Email

class Reuniao(models.Model):
    class Meta:
        ordering = ('assunto', )
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reuniões'

    assunto = models.CharField(max_length=255)
    texto = models.TextField()
    data = models.DateTimeField()
    emails = models.ManyToManyField(Email)

    def __unicode__(self):
        return self.assunto
