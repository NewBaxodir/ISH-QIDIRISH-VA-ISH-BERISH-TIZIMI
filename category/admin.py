from django.contrib import admin

from category.models import Citizenship, Uzbekiston_provinces, Uzbekiston_region

admin.site.register(Citizenship)
admin.site.register(Uzbekiston_provinces)
admin.site.register(Uzbekiston_region)




from category.models import Specialization
admin.site.register(Specialization)



from category.models import Relocation, Employment, Schedule

admin.site.register(Relocation)
admin.site.register(Employment)
admin.site.register(Schedule)




from category.models import Professiona, Thchoprofar

admin.site.register(Professiona)
admin.site.register(Thchoprofar)
