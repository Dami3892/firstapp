from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import users
from codes.forms import CodeForm
from users.models import CustomerUser
from .utils import send_sms

@login_required
def home_view(request):
    return render(request,'main.html', {})

def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        authenticate(request,username=username, password=password)
        if users is not None:
            request.session['pk'] = users.pk
            return redirect('verify-view')
        return render(request,'auth.html',{'form': form})

def verify_view(request):
        form= CodeForm(request.POST or None)
        pk = request.session.get('pk')
        if pk:
            users = CustomerUser.objects.get(pk=pk)
            code = users.code
            code_user = f"(username): {users.code}"
            if not request.POST:
                print(code_user)
                send_sms(code_user, users.phone_number)
            if form.is_valid():
                num = form.cleaned_data.get('number')

                if str(code) == num:
                     code.save()
                     login(request, users)
                     return redirect('home-view')
                else:
                    return redirect('login-view')
        return render(request, 'verify.html', {'form':form})


