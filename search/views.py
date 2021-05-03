from django.shortcuts import render
from summary.models import Summary
from jobs.models import Vacanciess
from accounts.filters import VacanciessFilter, SummaryFilter


# def search(request):
#     street = Streets.objects.all()
#     photo = Photo.objects.all()

#     filter = AnnouncementFilter(request.GET, queryset=Announcement.objects.all())
#     object_list = filter.qs

#     paginator = Paginator(object_list, 20)
#     page = request.GET.get('page')
#     object_list = paginator.get_page(page)
#     context = {"object_list": object_list, "filter": filter, "street": street, "photo": photo}
#     return render(request, 'search/search.html', context)


# Create your views here.
def search_summys(request):
	filter = SummaryFilter(request.GET, queryset=Summary.objects.all())
	object_list = filter.qs
	context = {"object_list": object_list, "filter":filter}
	return render(request, 'search/search_summys.html', context)




def search_jobs(request):
	filter = VacanciessFilter(request.GET, queryset=Vacanciess.objects.all())
	object_list = filter.qs
	context = {"object_list": object_list, "filter":filter}
	return render(request, 'search/search_jobs.html', context)


