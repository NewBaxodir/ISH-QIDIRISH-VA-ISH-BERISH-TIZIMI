from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth import authenticate, login as dj_login
from django.views.generic import CreateView, ListView, View
from django.contrib import messages
from accounts.models import User, Vacancies
from accounts.forms import UserSignUpForm, UservacanciesSignUpForm
from category.models import Uzbekiston_provinces, Uzbekiston_region
from summary.models import Summary
from jobs.models import Vacanciess


# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START HOME - BOSH SAHIFA ********************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# home page
def home(request):
    summs = Summary.objects.count()
    jobs = Vacanciess.objects.count()
    context = {"summs": summs, "jobs": jobs}
    return render(request, 'home/home.html', context)


def signin_su(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('account')
        else:
            messages.info(request, 'Login yoki Parolingiz xato.')
    context = {}
    return render(request, 'home/signin_su.html',context)



class signup_su(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'home/signup_su.html'
    
    def form_valid(self, form):
        user = form.save()
        # dj_login(self.request, user)
        return redirect('signin_su')




def signin_va(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('company')
        else:
            messages.info(request, 'Login yoki Parolingiz xato.')
    context = {}
    return render(request, 'home/signin_va.html',context)




class signup_va(CreateView):
    model = User
    form_class = UservacanciesSignUpForm
    template_name = 'home/signup_va.html'

    def form_valid(self, form):
        user = form.save()
        # dj_login(self.request, user)
        return redirect('signin_va')





# logout - logindan chiqish
def logout_view(request):
    logout(request)
    return redirect('home')





def load_cities(request):
    user_id = request.GET.get('user_id')
    cities = Uzbekiston_region.objects.filter(user_id=user_id).all()
    return render(request, 'home/city_dropdown_list_options.html', {'cities': cities})


# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END HOME - BOSH SAHIFA **********************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕