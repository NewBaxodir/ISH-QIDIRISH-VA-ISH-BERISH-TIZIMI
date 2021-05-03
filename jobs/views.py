from django.shortcuts import render
from jobs.models import Vacanciess
from accounts.forms import VacanciessForm
from category.models import Uzbekiston_provinces, Uzbekiston_region, Professiona, Thchoprofar
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.contrib import messages
from django.views.generic import CreateView, ListView, View
from django.shortcuts import redirect, render, get_object_or_404



# Create your views here.
def jobs(request):
    vacan = Vacanciess.objects.filter(user=request.user)
    context = {"vacan": vacan}
    return render(request, 'jobs/jobs.html', context)


def job_create(request):
    return render(request, 'jobs/job_create.html')

def job_create(request): 
    context = {}   
    form = VacanciessForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:                
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.user = request.user
                    student.save()
                    form.save_m2m()

            except IntegrityError:
                print("Error Encountered")

            return redirect('jobs')

    context['form'] = form
    return render(request, 'jobs/job_create.html', context)





def job_update(request, pk):
    vacan = get_object_or_404(Vacanciess, pk=pk)
    form = VacanciessForm(request.POST or None, instance=vacan)
    if form.is_valid():
        form.save()
        return redirect('jobs')
    context = {"form": form}
    return render(request, 'jobs/job_update.html', context)



# def job_delete(request, pk):
#     obj = get_object_or_404(Announcement, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#         # if form.is_valid():
#         return redirect('announcement')
#     context = {"obj": obj}
#     return render(request, 'announcements/job_delete.html', context)




def load_cities(request):
    user_id = request.GET.get('user_id')
    cities = Uzbekiston_region.objects.filter(user_id=user_id).all()
    return render(request, 'jobs/city_dropdown_list_options.html', {'cities': cities})



def load_citiess(request):
    user_id = request.GET.get('user_id')
    citiess = Thchoprofar.objects.filter(user_id=user_id).all()
    return render(request, 'jobs/city_dropdown_list_optionss.html', {'citiess': citiess})

