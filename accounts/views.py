
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, Confirm_Account, Reset_Password
from django.contrib.auth import authenticate, login, logout
from .forms import signup_form, signin_form, profile_form, resetpassword
from .string_gen import code, code2
from .send_email import send_email, send_email_resetpass
from django.conf import settings



# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = signup_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password1 = form.cleaned_data["password1"]
                password2 = form.cleaned_data["password2"]  
                
                user = User.objects
                if password1 == password2:
                    if not user.filter(username=username).exists():
                        if not user.filter(email=email).exists():
                            user = user.create_user(username=username, email=email, password=password2)
                            user.save()
                            UserProfile.objects.create(user=user).save()
                            gen = code()
                            confirm = Confirm_Account.objects.create(user=user.userprofile, key=gen)
                            confirm.save()
                            url = f'{settings.SEND_EMAIL_URL}accounts/confirm/{gen}'

                            send_email(receiver_email=user.email, username=user.username, href=url)
                            messages.info(request, 'يجب عليك تفعيل حسابك تم ارسال رسالة الى بريدك الالكتروني')
                            return redirect('signin')
                        else:
                            messages.info(request, 'بريد الالكتروني موجود من قبل')
                    else: 
                        messages.info(request, 'اسم المستخدم موجود من قبل')
                else:
                    messages.info(request, "كلمة المرور غير متطابقة")       
            else:

                messages.info(request, "خطاء في البيانات")

        else:
            form = signup_form

        return render(request, 'accounts/signup.html', {'form':form})
    else:
        return redirect('index')



def signin(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = signin_form(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data['username_or_email']
                password = form.cleaned_data['password']
                try:
                    user = User.objects.get(email=username_or_email)
                    username_or_email = user.username
                    
                except:
                    user = authenticate(request, username=username_or_email, password=password)
        
                if user is not None:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'خطاء في كلمة المرور او في البريد الالكتروني')
            else:
                messages.info(request, 'خطاء في البيانات')
        else:
            form = signin_form()

        return render(request, 'accounts/signin.html', {'form':form})
    else:
        return redirect('index')


def Logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')
    


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = profile_form(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone = form.cleaned_data['phone']
                city = form.cleaned_data['city']
                img = form.cleaned_data['img']
                
                
                user = User.objects.get(id=request.user.id)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                userprofile = UserProfile.objects.get(user=user)
                userprofile.phone = phone
                userprofile.city = city
                userprofile.save()
                
                if userprofile.img and img:
                    if "user.png" not in str(userprofile.img):
                        userprofile.img.delete()
                    userprofile.img = img
                    userprofile.save()
                else:
                    return redirect("profile")
                
                

        else:
            user = User.objects.get(id=request.user.id)
            userprofile = UserProfile.objects.get(user=user)
            form = profile_form()
            first_name = form['first_name'].as_widget(attrs={'value': user.first_name})
            last_name = form['last_name'].as_widget(attrs={'value': user.last_name})
            phone = form['phone'].as_widget(attrs={'value': userprofile.phone})
            city = form['city'].as_widget(attrs={'value': userprofile.city})
            form2 = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'city' : city,
                'img': form["img"]
            }
            
            return render(request, 'accounts/profile.html', {'form2':form2})

        return render(request, 'accounts/profile.html', {'form':form})
    return redirect('index')




def confirm_account(request, code):
    try:
        confirm = Confirm_Account.objects.get(key=code)
        
        userprofile = UserProfile.objects.get(user=confirm.user.user)
        userprofile.is_actived = True
        userprofile.save()
        confirm.delete()
        messages.info(request, 'تم تفعيل حسابك بنجاح')
        return redirect('profile')

    except:
            return redirect('error')


def SendConfirm(request):
    if request.user.is_authenticated:
        if not request.user.userprofile.is_actived:
            try:
                user = request.user
                Code = code()
                url = f'{settings.SEND_EMAIL_URL}accounts/confirm/{Code}'
                Confirm_Account.objects.filter(user=user.userprofile).delete()
                Confirm_Account.objects.create(user=user.userprofile, key=Code).save()
                send_email(user.email, user.username, url)

                messages.info(request, 'تم ارسال التفعيل الى بريدك الالكتروني')
                return redirect('profile')
            except:
                return redirect('error')
    return redirect('profile')



def error(request):
    return render(request, 'accounts/error.html')



def resetPassword(request, key):
    
    if request.method =='POST':
        form = resetpassword(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                try:
                    reset = Reset_Password.objects.get(key=key)
                    user = User.objects.get(id=reset.user.id)
                    user.set_password(password1)
                    user.save()
                    reset.delete()
                    return redirect('signin')
                except:
                    return redirect('error')
                

            else:
                messages.info(request, 'كلمة المرور غير متطابقة')
        else:
            messages.info(request, 'خطاء في ادخال البيانات')
    else:
        form = resetpassword()

    return render(request, 'accounts/resetPassword.html', {'form':form, 'key':key})


def resetPasswordGen(request):
    if request.user.is_authenticated:
        try:
            key = code2()
            user = request.user
            Reset_Password.objects.filter(user=user).delete()
            resetpassword = Reset_Password.objects.create(user=user, key=key)
            resetpassword.save()
            url = f"{settings.SEND_EMAIL_URL}accounts/resetpassword/{key}"

            send_email_resetpass(user.email, user.username, url)
            messages.info(request, 'تم ارسال رسالة الى بريدك الالكتروني لتغير كلمة المرور')
            return redirect('profile')
        except:
            return redirect('error')
        
        
    else:
        try:
            if request.method == 'POST':
                key = code2()
                email = request.POST['email']
                try:
                    user = User.objects.get(email=email)
                except:
                    messages.info(request, 'لم يتم العثور على بريدك الالكتروني')
                    return redirect('error')
                Reset_Password.objects.filter(user=user).delete()
                resetpassword = Reset_Password.objects.create(user=user, key=key)
                resetpassword.save()
                url = f"{settings.SEND_EMAIL_URL}accounts/resetpassword/{key}"
                send_email_resetpass(user.email, user.username, url)
                messages.info(request, 'تم ارسال رسالة الى بريدك الالكتروني لتغير كلمة المرور')
                return redirect('signin')
        except:
            return redirect('error')

        return render(request, 'accounts/emailResetPassword.html')
