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

from jobs.models import Vacanciess
from accounts.filters import VacanciessFilter





def account(request):
    filter = VacanciessFilter(request.GET, queryset=Vacanciess.objects.all())
    object_list = filter.qs
    context = {"object_list": object_list, "filter":filter}
    return render(request, 'accounts/account.html', context)



def account_info(request):
    return render(request, 'accounts/account_info.html')



def account_update(request, pk):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Wrong username or password.')
            return redirect('account_info')
        else:
            messages.info(request, 'Wrong username or password.')
    else:
        form = UserForm(instance=request.user)
        context = {"form": form}
    return render(request, 'accounts/account_update.html', context)




def account_delete(request, pk):
    com = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        com.delete()
        # if form.is_valid():
        return redirect('home')
    context = {"com": com}
    return render(request, 'accounts/account_delete.html', context)




