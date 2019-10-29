from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def login(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = auth.authenticate(username= username, password= password)

        if user is not None:
          auth.login(req,user)
          messages.add_message(req,messages.SUCCESS,'Oturum Açıldı')
          return redirect("index")
        else:
         messages.add_message(req,messages.ERROR,'kullanıcı adı veya parola yanlış')
         return redirect("login")
    else:
     return render(req,'user/login.html')


def register(req):
    if req.method == 'POST':
        username = req.POST["username"]
        email = req.POST["mail"]
        password = req.POST["password"]
        repassword = req.POST["repassword"]

        if password == repassword:
            # username ctrl
            if User.objects.filter(username = username).exists():
                messages.add_message(req,messages.WARNING,'bu kullanıcı kayıtlı daha önceden kayıt edilmiş')
                return redirect("register")
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(req,messages.WARNING,'bu mail adresi daha önceden oluşturulmuş')
                    return redirect("register")
                else:
                    user = User.objects.create_user(username = username, password=password, email=email)
                    user.save() 
                    messages.add_message(req,messages.SUCCESS,'kullanıcı oluşturuldu')
                    return redirect("login")
        else:
            messages.add_message(req,messages.ERROR,'parolalar eşleşmiyor, kontrol ediniz')
            return redirect("register")
    else:
        return render(req,'user/register.html')


def logout(req):
    if req.method == "POST":
        auth.logout(req)
        messages.add_message(req,messages.SUCCESS,"oturum başarı ile sonlandırıldı")
        return redirect("index")