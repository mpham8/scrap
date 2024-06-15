from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, SharedList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def home(request):
  context = {}
  return render(request, 'agenda/home.html', context)


@login_required
def agenda(request):
  #future: make more algo efficient lookup table two users' id and it gives table
  user1_lookup = 'mpham8'
  user2_lookup = 'ipekicten'
  # user1 = get_object_or_404(User, username=user1_lookup)
  user2 = get_object_or_404(User, username=user2_lookup)

  if request.method == 'POST':
    pass
    #insert create task

  #create on friend accept
  # shared_list = SharedList.objects.create(user1=user1, user2=user2)



  shared_lists = SharedList.objects.filter(user1=request.user, user2=user2) | SharedList.objects.filter(user1=user2, user2=request.user)
  # bucket_list = shared_lists.filter(name = "Bucket List")
  tasks = Task.objects.filter(shared_list__in=shared_lists)
  context = {'shared_lists': shared_lists, 'tasks': tasks}
  
  return render(request, 'agenda/agenda.html', context)


def logoutPage(request):
  logout(request)
  return redirect('home')


def loginPage(request):
  page = 'login'
  if request.user.is_authenticated:
    return redirect('agenda')
  
  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    try:
      user = User.objects.get(username = username)
    except:
      messages.error(request, 'User does not exist.')

    user = authenticate(request, username = username, password = password)
    if user is not None:
      login(request, user)
      return redirect('agenda')
    else:
      messages.error(request, 'Username or password does not exist')

  context = {'page': page}
  return render(request, 'agenda/login_page.html', context)


def registerUser(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form =  UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit = False)
      user.username = user.username.lower()
      user.save()
      login(request, user)
      return redirect('home')
    else:
        messages.error(request, 'error')
  context = {'form': form}

  return render(request, 'agenda/login_page.html', context)