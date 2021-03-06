from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, DomainForm
from .models import domainUser
from django.template import RequestContext
from django.shortcuts import render


def index(request):
    return render(request, 'domains/index.html')


@login_required
def special(request):
    return HttpResponse("Ha inicidado sesión !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def createDominio(request):
    created = False
    if request.method == 'POST':
        domain_form = DomainForm(data=request.POST)
        if domain_form.is_valid():
            domain = domain_form.save(commit=False)
            domain.user = request.user
            domain.save()
            created = True
            # print(domain.domain, domain.domain_user, domain.passwrd, domain.user)
            # TODO Call script domain.domain, domain.domain_user, domain.passwrd, domain.user
        else:
            print(domain_form.errors)
    else:
        domain_form = DomainForm()
    return render(request, 'domains/domain.html', {'domain_form': domain_form, 'created': created})


@login_required
def dominios(request):
    domains_list = domainUser.objects.filter(user=request.user)

    context_dict = {'domains': domains_list}

    return render(request, 'domains/my_domains.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'domains/registro.html',
                  {'user_form': user_form, 'registered': registered})

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'domains/login.html', {})
