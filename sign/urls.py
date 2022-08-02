from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, UserUpdate, make_me_author

urlpatterns = [
    path('sign/login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('sign/logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('sign/signup/', RegistrationView.as_view(template_name='sign/signup.html'), name='signup'),
    path('user/<int:pk>', UserUpdate.as_view(), name='user_edit'),
    path('author/', make_me_author, name='make_me_author'),
]