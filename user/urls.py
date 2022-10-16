from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
urlpatterns = [
  path('signin/', signIn, name='user-signin'),
  path('logout/', signOut, name='user-signout'),
  path('signup/', signUp, name='user-signup'),
  path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
  path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
  path('password_reset_done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
  path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete')
]