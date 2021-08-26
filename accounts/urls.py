from django.urls import path
from . import views

urlpatterns =[
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('confirm/<str:code>', views.confirm_account, name="confirm"),
    path('sendconfirm', views.SendConfirm, name='SendConfirm'),
    path('error', views.error, name='error'),
    path('resetpassword/<str:key>', views.resetPassword, name='resetpassword'),
    path('resetPasswordGen', views.resetPasswordGen, name="resetPasswordGen"),
]