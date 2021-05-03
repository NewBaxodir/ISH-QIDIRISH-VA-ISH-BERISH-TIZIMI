from django.db import models
from django.contrib.auth.models import AbstractUser
# from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from category.models import Uzbekiston_provinces, Uzbekiston_region


# Foydalanuvchining autentifikatsiyasi
class User(AbstractUser):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)    
    email = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = '1. UMUMIY FOYDALANUVCHILAR BAZASI'
        verbose_name_plural = '1. UMUMIY FOYDALANUVCHILAR BAZASI'



 # Moderator yartish kengaytirilgan yordamchi model
class Vacancies(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_numer = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    vacan_image = models.ImageField(null=True, blank=True, upload_to='images/')
    name_company = models.CharField(max_length=100) 
    provinces = models.ForeignKey(Uzbekiston_provinces, models.SET_NULL, blank=True, null=True,)
    region = models.ForeignKey(Uzbekiston_region, models.SET_NULL, blank=True, null=True,)
    YJS = (
        ('юридического лица', 'юридического лица'),
        ('физическое лицо', 'физическое лицо'),
        ('другие', 'другие'),
        )
    choose = models.CharField(max_length =100,choices=YJS)

    def __str__(self):
        return '%s' %(self.user)

    class Meta:
        verbose_name = '2. ISH BERUVCHI FOYDALANUVCHILAR BAZASI'
        verbose_name_plural = '2. ISH BERUVCHI FOYDALANUVCHILAR BAZASI'






