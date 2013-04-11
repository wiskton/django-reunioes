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

    def save(self, *args, **kwargs):
        import datetime
        from django.conf import settings
        from django.template.loader import render_to_string
        from django.core.mail import send_mail

        if not self.id:
            enviar_email = True
        else:
            enviar_email = False

        super(Reuniao, self).save(*args, **kwargs)

        if enviar_email:
            # valores
            site = u'AVISO REUNIÃO'
            destino = []

            assunto = self.assunto
            texto = self.texto

            for e in self.emails.all():
                destino.append(e.email)

            context = {
                'site': site,
                'assunto': assunto,
                'texto': texto,
                'data': datetime.datetime.today,
            }

            email_message = render_to_string('contato.txt', context)
            from_email = u"{0} <{1}>".format(site, settings.EMAIL_HOST_USER)
            send_mail(u'{0} - {1}'.format(site, assunto), email_message, from_email, destino, fail_silently=False)
