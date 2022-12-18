from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic 
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory


# @ login_required
# def favourite_add(request, pk):
#     story = get_object_or_404(NewsStory, pk=pk)
#     if story.favourites.filter(id=request.user.id).exists():
#         story.favourites.remove(request.user)
#     else:
#         story.favourites.add(request.user)
#     return redirect('news:story', pk=story.id)

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'users/createAccount.html'

class AccountView(generic.DetailView):
    model = CustomUser
    template_name = "users/account.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user
    
class AuthorProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/authorProfile.html'
    context_object_name= 'author'



