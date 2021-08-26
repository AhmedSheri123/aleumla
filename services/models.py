from django.db import models
from django.utils import timezone
import math


# Create your models here.





class Type(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="Type/%Y/%M/%d", blank=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="City/%Y/%M/%d", blank=True)


    def __str__(self):
        return self.name


Materials_informtions = """|link id| |for dollars = 1 and set name (دولار)| |for Euros = 2 and set name (يورو)| |for golds = 3 and set name (ذهب)|  |for turkish = 4 and set name (ليرة تركية)|  |for saudi = 5 and set name (ريال سعودي)|"""


class Materials(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="Materials/%Y/%M/%d", blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    link = models.IntegerField(default=0)
    informtions = models.TextField(default=Materials_informtions)


    def __str__(self):
        return self.name + " link: " + str(self.link)

class Dollars(models.Model):
    name = models.CharField(max_length=100)
    buy = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)
    publish_date = models.DateTimeField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return  self.name +"|" + " المدينة: " + self.city.name


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return "منذ " + str(seconds) + " ثانية"
            
            else:
                return "منذ " + str(seconds) + " ثواني"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "منذ " + str(minutes)  + " دقيقة"
            
            else:
                return "منذ " + str(minutes)  + " دقيقة"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "منذ " + str(hours) + " ساعة"

            else:
                return "منذ " + str(hours) + " ساعات"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "منذ " + str(days) + " يوم"

            else:
                return "منذ " + str(days) + " ايام"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return "منذ " + str(months) + " شهر"

            else:
                return "منذ " + str(months) + " اشهر"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return "منذ " + str(years) + " سنة"

            else:
                return "منذ " + str(years) + " سنوات"















class Euros(models.Model):
    name = models.CharField(max_length=100)
    buy = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)
    publish_date = models.DateTimeField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return  self.name +"|" + " المدينة: " + self.city.name


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return "منذ " + str(seconds) + " ثانية"
            
            else:
                return "منذ " + str(seconds) + " ثواني"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "منذ " + str(minutes)  + " دقيقة"
            
            else:
                return "منذ " + str(minutes)  + " دقيقة"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "منذ " + str(hours) + " ساعة"

            else:
                return "منذ " + str(hours) + " ساعات"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "منذ " + str(days) + " يوم"

            else:
                return "منذ " + str(days) + " ايام"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return "منذ " + str(months) + " شهر"

            else:
                return "منذ " + str(months) + " اشهر"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return "منذ " + str(years) + " سنة"

            else:
                return "منذ " + str(years) + " سنوات"





class Turkish(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    buy = models.IntegerField(default=0, verbose_name='سعر الشراء')
    sell = models.IntegerField(default=0, verbose_name='سعر البيع')
    publish_date = models.DateTimeField(verbose_name='تاريخ النشر')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='النوع')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='المدينة')
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='المادة')


    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return  self.name +"|" + " المدينة: " + self.city.name

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return "منذ " + str(seconds) + " ثانية"
            
            else:
                return "منذ " + str(seconds) + " ثواني"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "منذ " + str(minutes)  + " دقيقة"
            
            else:
                return "منذ " + str(minutes)  + " دقيقة"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "منذ " + str(hours) + " ساعة"

            else:
                return "منذ " + str(hours) + " ساعات"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "منذ " + str(days) + " يوم"

            else:
                return "منذ " + str(days) + " ايام"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return "منذ " + str(months) + " شهر"

            else:
                return "منذ " + str(months) + " اشهر"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return "منذ " + str(years) + " سنة"

            else:
                return "منذ " + str(years) + " سنوات"





class Saudi(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    buy = models.IntegerField(default=0, verbose_name='سعر الشراء')
    sell = models.IntegerField(default=0, verbose_name='سعر البيع')
    publish_date = models.DateTimeField(verbose_name='تاريخ النشر')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='النوع')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='المدينة')
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='المادة')


    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return  self.name +"|" + " المدينة: " + self.city.name

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return "منذ " + str(seconds) + " ثانية"
            
            else:
                return "منذ " + str(seconds) + " ثواني"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "منذ " + str(minutes)  + " دقيقة"
            
            else:
                return "منذ " + str(minutes)  + " دقيقة"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "منذ " + str(hours) + " ساعة"

            else:
                return "منذ " + str(hours) + " ساعات"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "منذ " + str(days) + " يوم"

            else:
                return "منذ " + str(days) + " ايام"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return "منذ " + str(months) + " شهر"

            else:
                return "منذ " + str(months) + " اشهر"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return "منذ " + str(years) + " سنة"

            else:
                return "منذ " + str(years) + " سنوات"












class Golds(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    buy = models.IntegerField(default=0, verbose_name='سعر الشراء')
    sell = models.IntegerField(default=0, verbose_name='سعر البيع')
    score = models.IntegerField(default=21,verbose_name='عيار الذهب')
    publish_date = models.DateTimeField(verbose_name='تاريخ النشر')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='النوع')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='المدينة')
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='المادة')


    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return  self.name +"|" + " المدينة: " + self.city.name

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return "منذ " + str(seconds) + " ثانية"
            
            else:
                return "منذ " + str(seconds) + " ثواني"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "منذ " + str(minutes)  + " دقيقة"
            
            else:
                return "منذ " + str(minutes)  + " دقيقة"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "منذ " + str(hours) + " ساعة"

            else:
                return "منذ " + str(hours) + " ساعات"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "منذ " + str(days) + " يوم"

            else:
                return "منذ " + str(days) + " ايام"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return "منذ " + str(months) + " شهر"

            else:
                return "منذ " + str(months) + " اشهر"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return "منذ " + str(years) + " سنة"

            else:
                return "منذ " + str(years) + " سنوات"


class show_in_index(models.Model):
    is_show = models.BooleanField(default=False, verbose_name="اظهار في الصفحة الرئيسية")
    type = models.ForeignKey(Type, on_delete= models.CASCADE, verbose_name="النوع")
    city = models.ForeignKey(City, on_delete= models.CASCADE, verbose_name="المدينة")
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name="المادة")

    def __str__(self):
        return " النوع:" + self.type.name + ", المدينة:" + self.city.name + ", المادة: " + self.materials.name + ", show in index: " + str(self.is_show)




class Details(models.Model):
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name="المادة")
    city = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name="المدينة")
    score_for_gold = models.IntegerField(default=21, verbose_name="عيار الذهب")
    is_enable = models.BooleanField(default=True ,verbose_name='تفعيل')


    def __str__(self):
        return " المادة:" + self.materials.name + ", المدينة:" + self.city.name + ", is_enabled:" + str(self.is_enable)