from django.shortcuts import render
from .forms import UsersForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    form = UsersForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Ro'yxatdan o'tdi")
        return HttpResponseRedirect('/')


    context = {
        'form': form,
    }
    return render(request, 'index.html',context)