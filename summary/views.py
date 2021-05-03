from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView, ListView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.contrib import messages
# Create your views here.
from accounts.models import User, Vacancies
from summary.models import Summary, Workexperience
from accounts.forms import UserForm, UserSignUpForm, UservacanciesSignUpForm, SummaryForm, WorkexperienceForm
from category.models import Uzbekiston_provinces, Uzbekiston_region




# Tarjimai hollar function
def summary(request):
    summ = Summary.objects.filter(user=request.user)
    context = {"summ": summ}
    return render(request, 'summary/summary.html', context)



def summary_create(request):
    context = {}    
    WorkexperienceFormset = modelformset_factory(Workexperience, form=WorkexperienceForm)  
    form = SummaryForm(request.POST or None)
    formset = WorkexperienceFormset(request.POST or None, queryset= Workexperience.objects.none(), prefix='workexperience')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.user = request.user
                    student.save()
                    form.save_m2m()

                    for mark in formset:
                        data = mark.save(commit=False)
                        data.student = student
                        data.save()
            except IntegrityError:
                print("Error Encountered")

            return redirect('summary')


    context['formset'] = formset
    context['form'] = form
    return render(request, 'summary/summary_create.html', context)






def summary_update(request, pk):
    summa = get_object_or_404(Summary, pk=pk)
    form = SummaryForm(request.POST or None, instance=summa)
    if form.is_valid():
        form.save()
        return redirect('summary')
    context = {"form": form}
    return render(request, 'summary/summary_update.html', context)





def load_cities(request):
    user_id = request.GET.get('user_id')
    cities = Uzbekiston_region.objects.filter(user_id=user_id).all()
    return render(request, 'summary/city_dropdown_list_options.html', {'cities': cities})


