from accounts.forms import resetpassword
from django.contrib import admin
from .models import UserProfile, Confirm_Account, Reset_Password

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Confirm_Account)
admin.site.register(Reset_Password)