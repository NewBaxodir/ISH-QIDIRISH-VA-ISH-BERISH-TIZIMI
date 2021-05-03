from django.db import models
from accounts.models import User
from category.models import Professiona, Thchoprofar, Uzbekiston_provinces, Uzbekiston_region
from ckeditor.fields import RichTextField




# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START резюме - Tarjimai xol
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
class Vacanciess(models.Model):
	title = "E'lon ish o'rni"
	pub_date = models.DateTimeField(auto_now_add=True)
	
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	
	title1 = "Asosiy ma'lumotlar"
	job_title = models.CharField(max_length=100, verbose_name="Lavozim")
	job_code = models.CharField(max_length=100, verbose_name="Ish kodi")
	profess = models.ForeignKey(Professiona, models.SET_NULL, blank=True, null=True,)
	thchopr = models.ForeignKey(Thchoprofar, models.SET_NULL, blank=True, null=True,)
	description = RichTextField(blank=True, null=True)

	MONEY = (
        ('USD', "USD"),
        ('RUB', "RUB"),
        ("UZS", "UZS"),
    )
	moneys = models.CharField(max_length =100, choices = MONEY)
	thesalaryfrom = models.CharField(max_length=100, verbose_name="$$$")
	thesalaryto = models.CharField(max_length=100, verbose_name="$$$")

	CHOOSEM = (
    ('до налогов', "до налогов"),
    ("в руках", "в руках"),
    )
	choosemo = models.CharField(max_length =100, choices = CHOOSEM)


	title2 = "Ish joyi"
	provinces = models.ForeignKey(Uzbekiston_provinces, models.SET_NULL, blank=True, null=True,)
	region = models.ForeignKey(Uzbekiston_region, models.SET_NULL, blank=True, null=True,)
	geolocation = models.CharField(max_length=100, verbose_name="Geo joylashuv")


	title3 = "Qo'shimcha"
	EMPLOYMENT = (
        ("Полная занятость", "Полная занятость"),
        ("Неполная занятость", "Неполная занятость"),
        ("Проектная работа или разовое задание", "Проектная работа или разовое задание"),
        ("Волонтерство", "Волонтерство"),
        ("Практика", "Практика"),
    )
	emptype = models.CharField(max_length =100, choices = EMPLOYMENT)
	WORKHO = (
        ("Полный день", "Полный день"),
        ("Сменная работа", "Сменная работа"),
        ("По таблицах", "По таблицах"),
        ("Долгая работа", "Долгая работа"),
    )
	worhou = models.CharField(max_length =100, choices = WORKHO)

	title4 = "Aloqa ma'lumotlari"
	name = models.CharField(max_length=100, verbose_name="Familya Ism")
	phone = models.CharField(max_length=100, verbose_name="Telefon nomer")
	comment = models.CharField(max_length=100, verbose_name="Siz bilan bog'lanishning qulay vaqti")


	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "E'LON ISH O'RNI"
		verbose_name_plural = "E'LON ISH O'RNI"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END резюме - Tarjimai xol
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕