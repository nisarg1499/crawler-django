from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


# def log(request):
# 	logout(request)
# 	return HttpResponse('Done logout')

def logout(request):
	logout(request)
	return HttpResponse('Done logout')

def signUp(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			return HttpResponse('Signup done')
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
		return render(request, 'signup.html', {'user_form' : user_form, 'registered': registered})


def login(request):
	if request.user.is_authenticated:
		return HttpResponse('Already logged in')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				auth_login(request, user)
				return render(request, 'index.html')
			else:
				return HttpResponse('Inactive')
		else:
			return HttpResponse('Invalid cred')
	else:
		return render(request, 'login.html', {})
