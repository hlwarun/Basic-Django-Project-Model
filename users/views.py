from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#This decorator tells that login is required to access the page
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   #Create an instance of class UserCreationForm
        if form.is_valid():
            form.save()          #saves the newly created user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, '{}, Account successfully created! You can now login!'.format(username))
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance = request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Congratulations! You have successfully updated your profile.')
        return redirect('profile')

    else:
        uform = UserUpdateForm(instance = request.user)
        pform = ProfileUpdateForm(instance = request.user.profile)


    context = {'uform':uform, 'pform':pform}
    return render(request, 'profile.html', context)
