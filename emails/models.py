# -*- coding: utf-8 -*-
from django.db import models

class Email(models.Model):

    class Meta:
        ordering = ('nome', )
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    nome = models.CharField(max_length=255)
    email = models.EmailField(verbose_name=u'Email', max_length=255)

    def __unicode__(self):
        return self.nome
