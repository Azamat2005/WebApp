from django.contrib import admin
from .models import User, Fanlar


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['Ism', 'Familya', 'Telefon', 'Fan']

class FanlarAdmin(admin.ModelAdmin):
    list_display = ('Fan', )



admin.site.register(User, UserAdmin)
admin.site.register(Fanlar, FanlarAdmin)