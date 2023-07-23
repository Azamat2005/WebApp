from django import forms
from .models import User
from .models import Fanlar
class UsersForm(forms.ModelForm):
    FanlarNomi = Fanlar.objects.values_list('Fan')

    FanlarData = []

    for Fan in FanlarNomi:
        FanlarData.append((Fan[0], Fan[0]))


    Ism = forms.CharField(widget=forms.TextInput(attrs={'class':'ism-input'}))
    Familya = forms.CharField(widget=forms.TextInput(attrs={'class':'Familya-input'}))
    Telefon = forms.CharField(widget=forms.TextInput(attrs={'class':'Telefon-input'}))
    CHOICES = (
        ('Matematika', 'Matematika'),
        ('Fizika 2', 'Fizika'),
        ('Mental Arifmetika','Mental Arifmetika'),
        ('Ingliz tili', 'Ingliz tili'),
        ('Rus tili', "Rus tili")
    )
    Fan = forms.CharField(widget=forms.Select(attrs={'class':'Fan-Select'}, choices=set(FanlarData)))
    class Meta:
        model = User
        fields = "__all__"