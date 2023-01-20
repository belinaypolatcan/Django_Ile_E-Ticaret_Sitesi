from email.policy import default
from django.db import models
from django.db import connections

class Notebook(models.Model):
    marka = models.CharField(max_length=100)
    modelismi = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    model=models.CharField(max_length=100,null=True)
    fiyat = models.CharField(max_length=100)
    isletimsistemi = models.CharField(max_length=100)
    islemcimodeli = models.CharField(max_length=100)
    diskkapasitesi = models.CharField(max_length=100)
    bellekkapasitesi = models.CharField(max_length=100)
    ekrankartimodeli = models.CharField(max_length=100)
    siteismi = models.CharField(max_length=100)
    resim=models.CharField(max_length=100,null=True)
    
   

class Hepsiburada(models.Model):
    marka = models.CharField(max_length=100)
    modelismi = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    fiyat = models.CharField(max_length=100)
    isletimsistemi = models.CharField(max_length=100)
    islemcimodeli = models.CharField(max_length=100)
    diskkapasitesi = models.CharField(max_length=100)
    bellekkapasitesi = models.CharField(max_length=100)
    ekrankartimodeli = models.CharField(max_length=100)
    siteismi = models.CharField(max_length=100)
    resim=models.CharField(max_length=100,null=True)
    