from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="اسم المستخدم")
    phone = models.CharField(max_length=11, blank=True)
    img = models.ImageField(upload_to="accounts/%Y/%M/%d", verbose_name="صورة ملف الشخصي", blank=True, default="user.png")
    city = models.CharField(max_length=50, blank=True)
    is_actived = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class Confirm_Account(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=250, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username + ", تاريخ:" + str(self.pub_date)

class Reset_Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=400, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ", تاريخ:" + str(self.pub_date)

