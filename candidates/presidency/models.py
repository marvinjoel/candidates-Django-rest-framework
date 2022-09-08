from django.db import models
from datetime import datetime

from django.utils.safestring import mark_safe

from candidates.vpresidency.models import CongresistaModel, ParAndinoModel


class PoliticModel(models.Model):
    politc_p = models.CharField(max_length=300)

    def __str__(self):
        return self.politc_p

    class Meta:
        verbose_name ='Politic'
        verbose_name_plural = 'Politics'
        ordering = ['id']


class Studies(models.Model):
    studes = models.CharField(verbose_name='Estudios', max_length=500)

    def __str__(self):
        return self.studes

    class Meta:
        verbose_name='Stude'
        verbose_name_plural= 'Studes'
        ordering = ['id']


class PresidencyModel(models.Model):

    def pre_url(self, filename):
        ruta = f'media/candidate/presidency/{self.first_name}/{filename}'
        return ruta

    def photo_cant(self):
        return mark_safe(f'<img src="{self.photo}" width=50px height=50px />')

    first_name_pres = models.CharField(max_length=150)
    last_name_pres = models.CharField(max_length=150)
    birthday_pres = models.DateField(default=datetime.now)
    photo_pres = models.ImageField(upload_to=pre_url, blank=True, null=True)

    studes = models.ManyToManyField(Studies, blank=True, null=True)
    politic_part = models.OneToOneField(PoliticModel, on_delete=models.CASCADE, blank=True)

    congresista = models.ForeignKey(CongresistaModel, on_delete=models.CASCADE)
    parlamento_andino = models.ForeignKey(ParAndinoModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name_pres

    class Meta:
        verbose_name = 'Presiden'
        verbose_name_plural = 'Presidency'
        ordering = ['id']

