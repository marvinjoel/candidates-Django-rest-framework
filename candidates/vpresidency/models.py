from django.db import models


class CongresistaModel(models.Model):

    def Pcant_url(self, filename):
        ruta = f'media/candidate/congresista/first/{self.first_name}/{filename}'
        return ruta

    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.IntegerField()
    photo = models.ImageField(upload_to=Pcant_url, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Congresista'
        verbose_name_plural = 'Congresista'
        ordering = ['id']


class ParAndinoModel(models.Model):

    def Scant_url(self, filename):
        ruta = f'media/candidate/parandino/second/{self.first_name}/{filename}'
        return ruta

    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.IntegerField()
    photo = models.ImageField(upload_to=Scant_url, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Parlamento'
        verbose_name_plural = 'Parlamentos'
        ordering = ['id']