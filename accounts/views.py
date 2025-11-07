from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, UserProfileForm
from accounts.models import Profile
from courses.models import UserCourseProgress, UserTitle


# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('common:home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/sign_in.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('common:home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html')

def sign_out(request):
    logout(request)
    return redirect('common:home')

def profile_view(request):
    user =request.user
    completed_courses = UserCourseProgress.objects.filter(user=request.user, completed=True)
    titles = UserTitle.objects.filter(user=request.user)
    leaderboard = Profile.objects.all().order_by('-total_points')
    return render(request, 'accounts/profile.html', context={'user': user, 'completed_courses': completed_courses, 'titles': titles, 'leaderboard': leaderboard})

def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            profile_img = form.cleaned_data.get('profile_img')
            if profile_img:
                profile.profile_img = profile_img
            profile.save()

            return redirect('accounts:profile')
    else:
        form = UserProfileForm(
            instance=user,
            initial={
                'profile_img': profile.profile_img,
            }
        )

    return render(request, 'accounts/edit_profile.html', {'form': form})
