from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from .models import User


def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        form = RegistrationForm()
    else:
        form = RegistrationForm()

    data = User.objects.all()
    return render(request, 'crud/viewdata.html', {'form': form, 'data': data})


def delete(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


def update(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        form = RegistrationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        data = User.objects.get(pk=id)
        form = RegistrationForm(instance=data)

    return render(request, 'crud/update.html', {'form': form})
