from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, View
from django.db import transaction
from django.dispatch import receiver
# from django.forms import CheckboxSelectMultiple
# from multiselectfield import MultiSelectField
from .models import User, Vacancies
from summary.models import Summary, Workexperience
from category.models import Uzbekiston_provinces, Uzbekiston_region
from category.models import Citizenship, Specialization
from jobs.models import Vacanciess





# Change OneToOne form 
class UserForm(forms.ModelForm):
    last_name = forms.CharField(required=False, label="Familya", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Фамилия'}
        ))
    first_name = forms.CharField(required=False, label="Ism", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Имя'}
        ))   
    email = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Электронная почта'}
        ))
    username = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Логин'}
        ))
    # password = forms.CharField(required=False, widget=forms.TextInput(
    #     attrs = {'class':'form-control', 'placeholder': 'Parol'}
    #     ))


    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username')



class VacanciesForm(forms.ModelForm):
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Номер телефона'}
        ))
    name_company = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Названия компании'}
        ))

    class Meta:
        model = Vacancies
        fields = ('phone_numer', 'name_company', 'provinces', 'region')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provinces'].widget.attrs.update({'class': 'form-control rounded-1', 'placeholder': 'Login'}) 
        self.fields['region'].widget.attrs.update({'class': 'form-control rounded-1', 'placeholder': 'Login'}) 






# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
class UserSignUpForm(UserCreationForm):

    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Имя'}
        ))   
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autocomplete':'username', 'placeholder': 'Электронная почта'}
        ))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autocomplete':'username', 'placeholder': 'Логин'}
        ))
    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password', 'class':'form-control rounded-1', 'autocomplete':'current-password', 'placeholder': 'Пароль'}
        ))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control rounded-1', 'autocomplete':'current-password', 'placeholder': 'Повтор пароля'}
        ))
 
    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.first_name = self.cleaned_data.get('first_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        return user

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Login'}) 
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Parol'}) 
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Parolni qaytadan kiriting'}) 

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓




YJS = (
    ('юридического лица', 'юридического лица'),
    ('физическое лицо', 'физическое лицо'),
    ('другие', 'другие'),
    )

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

class UservacanciesSignUpForm(UserCreationForm):

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Фамилия'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Имя'}
        ))    
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Электронная почта'}
        ))
    name_company = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Названия компании'}
        ))
    choose = forms.ChoiceField(choices=YJS)
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': '+9'}
        ))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Логин'}
        ))
    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control rounded-1', 'placeholder': 'Пароль'}
        ))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control rounded-1', 'placeholder': 'Повтор пароля'}
        ))
    provinces = forms.ModelChoiceField(queryset=Uzbekiston_provinces.objects.all(), label="Viloyatlar", required=True)
    region = forms.ModelChoiceField(queryset=Uzbekiston_region.objects.all(), label="Tumanlar", required=True)

    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True

        if commit:
            user.save()
            group = Group.objects.get(name="vacancies")
            user.groups.add(group)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.username = self.cleaned_data.get('username')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.save()
        useradminpage = Vacancies.objects.create(user=user)
        useradminpage.phone_numer=self.cleaned_data.get('phone_numer')        
        useradminpage.name_company=self.cleaned_data.get('name_company')        
        useradminpage.provinces=self.cleaned_data.get('provinces')        
        useradminpage.region=self.cleaned_data.get('region')        
        useradminpage.choose=self.cleaned_data.get('choose')        
        useradminpage.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provinces'].widget.attrs.update({'class': 'form-control rounded-1'}) 
        self.fields['region'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['choose'].widget.attrs.update({'class': 'form-control rounded-1'})

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓












SEX = (
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
    )

WORKEX = (
    ("Есть опыт работы", "Есть опыт работы"),
    ("Нет опыта работы", "Нет опыта работы"),
    )
MONEY = (
    ('USD', "USD"),
    ('RUB', "RUB"),
    ("UZS", "UZS"),
    )

class SummaryForm(forms.ModelForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Фамилия'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Имя'}
        ))
    phone_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': '+9 '}
        ))
    data_time = forms.DateField(required=True, widget=forms.DateInput(
        attrs = {'type': 'date', 'class':'form-control rounded-1'}
        ))

    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX)
    citizenship = forms.ModelMultipleChoiceField(queryset=Citizenship.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    workexper = forms.ChoiceField(widget=forms.RadioSelect, choices=WORKEX)
    
    moneys = forms.ChoiceField(required=False, choices=MONEY)
    speciali = forms.ModelMultipleChoiceField(queryset=Specialization.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)

    thesalary = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': ''}
        ))
    carobjec = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': ''}
        ))
    key_skills = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text','style':'height: 100px', 'placeholder': ""}
        ))

    class Meta:
        model = Summary
        fields = ('last_name', 'first_name', 'phone_name', 'provinces', 'region', 'data_time', 'sex', 'citizenship', 'workexper', 'thesalary', 'carobjec', 'key_skills', 'moneys', 'speciali', 'profess', 'thchopr', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provinces'].widget.attrs.update({'class': 'form-control rounded-1'}) 
        self.fields['region'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['moneys'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['profess'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['thchopr'].widget.attrs.update({'class': 'form-control rounded-1'})
        
        self.fields['image1'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['image2'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['image3'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['image4'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['image5'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['image6'].widget.attrs.update({'class': 'form-control rounded-1'})




class WorkexperienceForm(forms.ModelForm):
    begwork = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control rounded-1 formset-field'}))
    finishw = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control rounded-1 formset-field'}))
    organiza = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control rounded-1 formset-field'}))
    position = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control rounded-1 formset-field'}))
    workplaceres = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control rounded-1 formset-field', 'style':'height: 50px'}))

    class Meta:
        model = Workexperience

        fields = [
            'begwork',
            'finishw',
            'organiza',
            'position',
            'workplaceres',
        ]

        # widgets = {
        #     'begwork': forms.DateInput(attrs={'type': 'date', 'class': 'formset-field'}),
        #     'finishw': forms.DateInput(attrs={'type': 'date', 'class': 'formset-field'}),
        #     'organiza': forms.TextInput(attrs={'class': 'formset-field'}),
        #     'position': forms.TextInput(attrs={'class': 'formset-field'}),
        #     'workplaceres': forms.Textarea(attrs={'class': 'formset-field'}),
        # }













CHOOSEM = (
    ('до налогов', "до налогов"),
    ("в руках", "в руках"),
    )

EMPLOYMENT = (
    ("Полная занятость", "Полная занятость"),
    ("Неполная занятость", "Неполная занятость"),
    ("Проектная работа или разовое задание", "Проектная работа или разовое задание"),
    ("Волонтерство", "Волонтерство"),
    ("Практика", "Практика"),
    )

WORKHO = (
    ("Полный день", "Полный день"),
    ("Сменная работа", "Сменная работа"),
    ("По таблицах", "По таблицах"),
    ("Долгая работа", "Долгая работа"),
    )

class VacanciessForm(forms.ModelForm):
    job_title = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': ''}
        ))
    job_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': ''}
        ))
    thesalaryfrom = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'от'}
        ))
    thesalaryto = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'до'}
        ))
    choosemo = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOOSEM)
    geolocation = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': ''}
        ))
    emptype = forms.ChoiceField(widget=forms.RadioSelect, choices=EMPLOYMENT)
    worhou = forms.ChoiceField(widget=forms.RadioSelect, choices=WORKHO)
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': ''}
        ))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': '+9'}
        ))
    comment = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', "placeholder": ""}
        ))

    class Meta:
        model = Vacanciess
        fields = (
            'job_title', 'job_code', 'profess', 'thchopr', 'description', 'moneys',
            'thesalaryfrom', 'thesalaryto', 'choosemo', 'provinces', 'region', 'geolocation', 'emptype',
            'worhou', 'name', 'phone', 'comment'
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profess'].widget.attrs.update({'class': 'form-control rounded-1'}) 
        self.fields['thchopr'].widget.attrs.update({'class': 'form-control rounded-1'}) 
        self.fields['moneys'].widget.attrs.update({'class': 'form-control rounded-1'})
        self.fields['provinces'].widget.attrs.update({'class': 'form-control rounded-1'}) 
        self.fields['region'].widget.attrs.update({'class': 'form-control rounded-1'}) 
  
