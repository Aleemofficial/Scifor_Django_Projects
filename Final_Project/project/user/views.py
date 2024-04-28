from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#################### index####################################### 
def index(request):
	return render(request, 'user/index.html', {'title':'CreativeHub'})

########### register here ##################################### 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
    next_page = request.POST.get('next', request.GET.get('next', 'home'))
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Thankyou {username}!')
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'Log in', 'next': next_page})


def home(request):
    return render(request, 'user/home.html')

def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})


@login_required
def aboutus(request):
    # Logic to handle settings page
    return render(request, 'user/aboutus.html')

def art_page(request):
    # Logic to fetch data or perform any other operations
    return render(request, 'user/art_page.html')

def write_page(request):
    # Logic to fetch data or perform any other operations
    return render(request, 'user/write_page.html')

def music_page(request):
    # Logic to fetch data or perform any other operations
    return render(request, 'user/music_page.html')

def puzzles_page(request):
    # Logic to fetch data or perform any other operations
    return render(request, 'user/puzzles_page.html')
