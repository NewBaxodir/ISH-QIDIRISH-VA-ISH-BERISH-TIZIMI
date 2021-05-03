from django.contrib import admin
from accounts.models import User, Vacancies
admin.site.register(User)
admin.site.register(Vacancies)
# Register your models here.



# # Register your models here.
admin.site.site_header = 'MASTERUZ.UZ - SUPER MODERATOR'
admin.site.site_title = 'DAVIROV - OCHILOV'
admin.site.index_title = 'BAKHODIR DAVIROV - FARKHOD OCHILOV'