from django.shortcuts import render
from accounts.models import User, Vacancies
from summary.models import Summary, Workexperience
from accounts.forms import UserForm, VacanciesForm, UserSignUpForm, UservacanciesSignUpForm, SummaryForm, WorkexperienceForm
from django.contrib import messages

from django.views.generic import CreateView, ListView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
from jobs.models import Vacanciess
from accounts.filters import VacanciessFilter, SummaryFilter





@allowed_users(allowed_roles=['vacancies'])
def company(request):
    filter = SummaryFilter(request.GET, queryset=Summary.objects.all())
    object_list = filter.qs
    context = {"object_list": object_list, "filter":filter}
    return render(request, 'company/company.html', context)




def company_info(request):
    return render(request, 'company/company_info.html')



def company_update(request, pk):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        profile_form = VacanciesForm(request.POST,request.FILES, instance=request.user.vacancies)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.info(request, 'Wrong username or password.')
            return redirect('company_info')
        else:
            messages.info(request, 'Wrong username or password.')
    else:
        form = UserForm(instance=request.user)
        profile_form = VacanciesForm(instance=request.user.vacancies)
    return render(request, 'company/company_update.html', {
        'form': form,
        'profile_form': profile_form
    })



def company_delete(request, pk):
    com = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        com.delete()
        # if form.is_valid():
        return redirect('home')
    context = {"com": com}
    return render(request, 'company/company_delete.html', context)

