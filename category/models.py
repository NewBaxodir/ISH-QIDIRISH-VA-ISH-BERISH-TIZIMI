from django.db import models





# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START Гражданство - Fuqarolik
class Citizenship(models.Model):
	title = "Fuqarolik"
	name = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "1. FUQAROLIK (BAZASI)"
		verbose_name_plural = "1. FUQAROLIK (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕







# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START Город проживания - Yashash shahri
class Uzbekiston_provinces(models.Model):
	title = "Uzbekiston viloyatlari"
	provinces = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.provinces
	class Meta:
		verbose_name = "2. O'ZBEKISTON VILOYATLARI (BAZASI)"
		verbose_name_plural = "2. O'ZBEKISTON VILOYATLARI (BAZASI)"

# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

class Uzbekiston_region(models.Model):
	title = "Uzbekiston tumanlari"
	user = models.ForeignKey(Uzbekiston_provinces, on_delete = models.CASCADE)
	region = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.region
	class Meta:
		verbose_name = "3. O'ZBEKISTON TUMANLAR (BAZASI)"
		verbose_name_plural = "3. O'ZBEKISTON TUMANLAR (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕





# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START Переезд - Boshqa joyga ko'chirish
class Relocation(models.Model):
	title = "Boshqa joyga ko'chirish"
	name = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "BOSHQA JOYGA KO'CHISH (BAZASI)"
		verbose_name_plural = "BOSHQA JOYGA KO'CHISH (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕




# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START Занятость - Bandlik
class Employment(models.Model):
	title = "Bandlik"
	name = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "BANDLIK (BAZASI)"
		verbose_name_plural = "BANDLIK (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START График работы - Ish grafigi
class Schedule(models.Model):
	title = "Ish grafigi"
	name = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "ISH GRAFIGI (BAZASI)"
		verbose_name_plural = "ISH GRAFIGI (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


























# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START Специализации - Mutaxassisliklar **********************
class Specialization(models.Model):
	title = "Mutaxassisliklar tajriba yuq"
	name = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "MUTAXASSISLIKLAR TAJRIBA YO'Q (BAZASI)"
		verbose_name_plural = "MUTAXASSISLIKLAR TAJRIBA YO'Q (BAZASI)"
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕





class Professiona(models.Model):
	title = "Professional yo'nalish"
	profarea = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.profarea
	class Meta:
		verbose_name = "01. PROFESSIONAL BO'LIM (Tajribali ishchilar)"
		verbose_name_plural = "01. PROFESSIONAL YO'NALISH (Tajribali ishchilar)"


class Thchoprofar(models.Model):
	title = "Mutaxasisliklar"
	user = models.ForeignKey(Professiona, on_delete = models.CASCADE)
	profar = models.CharField(max_length=100, verbose_name="Nomi")

	def __str__(self):
		return self.profar
	class Meta:
		verbose_name = "02. MUTAXASISLIKLAR (Tajribali ishchilar)"
		verbose_name_plural = "02. MUTAXASISLIKLAR (Tajribali ishchilar)"















