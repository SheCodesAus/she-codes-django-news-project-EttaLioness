from django.urls import path 
from .views import CreateAccountView, AccountView, AuthorProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('authorProfile/<int:pk>/', AuthorProfileView.as_view(), name='authorProfile'),
    path('<int:pk>/' , AccountView.as_view(), name="user"),
]