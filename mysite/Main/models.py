from django.db import models

# Create your models here.

class Firms(models.Model):
    firm_id = models.CharField('id', max_length=10)
    firm_name = models.CharField('name', max_length=20)

    def __str__(self):
        return self.firm_name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Types(models.Model):
    type_id = models.CharField('id', max_length=10)
    type_name = models.CharField('name', max_length=20)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Technic(models.Model):
    technic_id = models.CharField('id', max_length=10)
    technic_name = models.CharField('name', max_length=50)
    firm = models.ForeignKey(Firms, on_delete=models.CASCADE)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return self.technic_name