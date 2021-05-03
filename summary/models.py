from django.db import models
from accounts.models import User
from category.models import Uzbekiston_provinces, Uzbekiston_region
from category.models import Citizenship, Specialization, Professiona, Thchoprofar

# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START резюме - Tarjimai xol
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
class Summary(models.Model):
	title = "Tarjimai hol"
	pub_date = models.DateTimeField(auto_now_add=True)
	
	title1 = "Aloqa ma'lumotlari"
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	last_name = models.CharField(max_length=100, verbose_name="Familya")
	first_name = models.CharField(max_length=100, verbose_name="Ism")
	phone_name = models.CharField(max_length=100, verbose_name="Telefon nomer")

	provinces = models.ForeignKey(Uzbekiston_provinces, models.SET_NULL, blank=True, null=True,)
	region = models.ForeignKey(Uzbekiston_region, models.SET_NULL, blank=True, null=True,)
	
	

	title2 = "Asosiy ma'lumotlar"
	data_time = models.DateField()

	SEX = (
		('Мужской', 'Мужской'),
		('Женский', 'Женский'),
        )
	sex = models.CharField(max_length =100, choices = SEX)
	citizenship = models.ManyToManyField(to='category.Citizenship')

	
	WORKEX = (
		("Есть опыт работы", "Есть опыт работы"),
		("Нет опыта работы", "Нет опыта работы"),
        )
	workexper = models.CharField(max_length =100, choices = WORKEX)
	carobjec = models.CharField(max_length=100, verbose_name="Kareriya maqsadi")
	key_skills = models.TextField(verbose_name="Talluqli soxalar")
	
	thesalary = models.CharField(max_length=100, verbose_name="$$$")
	MONEY = (
        ('USD', "USD"),
        ('RUB', "RUB"),
        ("UZS", "UZS"),
    )
	moneys = models.CharField(max_length =100, choices = MONEY)
	speciali = models.ManyToManyField(to='category.Specialization')
	profess = models.ForeignKey(Professiona, models.SET_NULL, blank=True, null=True,)
	thchopr = models.ForeignKey(Thchoprofar, models.SET_NULL, blank=True, null=True,)


	image1 = models.ImageField(null=True, blank=True, upload_to='images/')
	image2 = models.ImageField(null=True, blank=True, upload_to='images/')
	image3 = models.ImageField(null=True, blank=True, upload_to='images/')
	image4 = models.ImageField(null=True, blank=True, upload_to='images/')
	image5 = models.ImageField(null=True, blank=True, upload_to='images/')
	image6 = models.ImageField(null=True, blank=True, upload_to='images/')


	def __str__(self):
		return self.carobjec

	def num_id(self):
		return self.id.all().count()


	class Meta:
		verbose_name = "E'LON TARJIMAI HOL"
		verbose_name_plural = "E'LON TARJIMAI HOL"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END резюме - Tarjimai xol
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


class Workexperience(models.Model):
    student = models.ForeignKey(Summary, null=True, blank=True, related_name = "workexperience", on_delete=models.CASCADE)
    begwork = models.DateField(null=True)
    finishw = models.DateField(null=True)
    organiza = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    workplaceres = models.TextField(blank=True, verbose_name="Ish joyingizdagi vazifa haqida yozing")

    class Meta:
        db_table = "workexperience"