from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# class Register(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'user/register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
#         return redirect('register')
class Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Corrected the condition
            form.save()
            return redirect('/')
        return redirect('register')


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/profile.html')
