from distutils.command.upload import upload
from turtle import back
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Collection(models.Model):
    name = models.CharField('Name of Collection',max_length=100)
    amount = models.IntegerField('Total number of coins in collection')
    status = models.BooleanField('Status', default=True)
    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.name

class Coin(models.Model):
    id_collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    coin_number = models.IntegerField('# Coin',null=False, blank=False)
    name = models.CharField('Name',max_length=100)
    year = models.IntegerField('Year of creation',null=False, blank=False)
    image = models.ImageField('Image')
    status = models.BooleanField('Status',default=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        verbose_name = "Coin"
        verbose_name_plural = "Coins"

    def __str__(self):
        return f'{self.year}--{self.name}'

class Collector(models.Model):
    username = models.CharField('UserName', max_length=50 , null=False, blank=False)
    password = models.CharField('Passaword', max_length=30, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False)
    coins = models.ManyToManyField(Coin, blank=True, null=True)
