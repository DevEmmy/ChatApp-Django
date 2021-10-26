from django.shortcuts import render
from .models import Group, Message
from .form import CreateGroup, SendMessage, RegisterUser
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

# Create your views here.
@login_required
def group_list(request):
	groups = Group.objects.all()
	context = {'groups':groups}
	return render(request, 'main/group_list.html', context)

@login_required
def create_group(request):
	form = CreateGroup()
	if request.method == 'POST':
		form = CreateGroup(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.slug = slugify(request.POST['group_name'])
			obj.save()
			return redirect('group_list')

	context = {'form':form}
	return render(request, 'main/create_group.html', context)

@login_required
def messages(request, slug):
	group = Group.objects.get(slug=slug)
	messages = group.message_set.all()
	context = {'messages':messages, 'group':group}
	return render(request, 'main/messages.html', context)

@login_required
def send_message(request, slug):
	if request.method == 'POST':
		form = SendMessage(request.POST)
		print(form)
		if form.is_valid():
			obj = form.save(commit=False)
			print(obj)
			obj.save()
			return redirect('messages', slug)
	return redirect('create_group')


def register_view(request):
	form = RegisterUser()
	if request.method == 'POST':
		form = RegisterUser(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			return redirect('group_list')
		else:
			context = {'form':form}
			return render(request, 'main/register.html', context)

	context = {'form':form}
	return render(request, 'main/register.html', context)



def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('group_list')
		else:
			message = 'Invalid Username or Password'
			context = {'message':message}
			return render(request, 'main/login.html', context)

	return render(request, 'main/login.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')