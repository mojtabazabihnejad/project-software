from django.shortcuts import render
from myapp.models import myuser
from myapp.models import myuserh
from myapp.models import hamayesh1
from myapp.models import myadmin
# from myapp.models import RSS
# from myapp.models import test
import feedparser
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect



def signup(request):

    if request.method=="GET":
        return render(request,'user/signup1.html')
    else :

        username=request.POST.get("username")
        kname=request.POST.get("kname")
        lname=request.POST.get("lname")
        password=request.POST.get("password")
        passwordc=request.POST.get("passwordc")
        email=request.POST.get("email")
        m=member.objects.filter(user=username)
        if len(m)==0:
            str1=""
            if len(password)==0:
                str1+=("پسوردی برای نام کاربری انتخاب نشده است")
                return render(request,'user/signup1.html',{'s':str1})
            if password!=passwordc:
                str1+=("پسووردها یکسان وارد نشده اند")
                return render(request,'user/signup1.html',{'s':str1})


            if len(str1)==0 :

                h=member(user=request.POST.get("username"),name=request.POST.get("kname"),
                          lastname=request.POST.get("lname"),pass1=request.POST.get("password"),email=request.POST.get("email"),type1="user")
                h.save()
                return render(request,'user/dashboard.html')


        else :
            str = ""
            str+=("این نام کاربری قبلا ثبت شده است")
            return render(request,'user/signup1.html',{'p':str})

#####################################################
def login(request):

    return render(request, 'user/login.html')
#####################################################
def save(request):

    list2=[]
    k=request.POST.get('newuser')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    pass1=request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    if k=='T':
        if pass1!=pass2:
            list2.append("password not match")
        if len(pass1)==0:
            list2.append("pass not incorect")

        if len(list2)==0 :

            h = myuser(fn=request.POST.get("fname"),ln=request.POST.get("lname"),
                     email=request.POST.get("email"),un=request.POST.get("username"),pw=request.POST.get("pass1"))
            h.save()
            return render(request,'user/save.html')
        else :
            return render(request,'user/signup.html',{'lst':list2})
    else:

        m= user.objects.filter(email =request.POST.get('oldemail'))[0]
        m.fn=fname
        m.ln=lname
        m.email=email
        m.un=username
        m.pw=pass1
        m.save()
        return HttpResponseRedirect("/user/")
#####################################################
def saveh(request,*args, **kwargs):

    k=request.POST.get('newuser')
    list2=[]
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    pass1=request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    num = request.POST.get('num')
    serialh = request.POST.get('serialh')
    p=hamayesh1.objects.filter(serial=serialh)
    if k == 'T':
        if len(p)==0:
            list2.append("thr seminar is not exist")
        if pass1!=pass2:
                list2.append("password not match")
        if len(pass1)==0:
                list2.append("pass not incorect")

        if len(list2)==0 :
             h=myuserh(fn=request.POST.get("fname"),
                       ln=request.POST.get("lname"),
                       email=request.POST.get("email"),
                       un=request.POST.get("username"),
                       pw=request.POST.get("pass1"),
                       num=request.POST.get("number"),
                       serial=request.POST.get("serialh"))
             h.save(args, kwargs)
             return render(request,'user/save.html')
        else :
             return render(request,'user/signup.html',{'lst':list2})
    else:

        m= userh.objects.filter(email =request.POST.get('oldemail'))[0]
        m.fn=fname
        m.ln=lname
        m.email=email
        m.un=username
        m.pw=pass1
        m.num=num
        m.serial=serialh
        m.save(args, kwargs)
        return HttpResponseRedirect("/userh/")
#####################################################
#####################################################
def user(request):

    # if not("login" in request.session):
    #     return render(request, 'user/login.html')
    # else:

        User=myuser.objects.all()
        return render(request,'user/users.html',{'k':User})
#####################################################
def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        if username == "admin" and password == "passadmin":
            User=myuser.objects.all()
            return render(request,'user/users.html',{'k':User})
        else:
            str = ""
            str += ("your name or password is wrong")
            return render(request, 'user/adminlogin.html',{'str':str})
    else:
        return render(request,'user/adminlogin.html')


#####################################################
def userdashboard(request):

    Msg=[]
    username = request.POST.get('username')
    password=request.POST.get('password')
    em= myuser.objects.filter(un=username,pw=password)
    if len(em)==0:
        Msg.append("password is wrong")
    if len(Msg) == 0:
        return render(request,'user/dashboard.html')
    else:
        return render(request, 'user/login.html',{'msg':Msg})
#####################################################
def userdashboardh(request):

    Msg=[]
    serial = request.POST.get('serial')
    email = request.POST.get('email')
    password=request.POST.get('password')
    ser = myuserh.objects.filter(serial=serial,email=email,pw=password)
    if len(ser)== 0:
        Msg.append("serial or password is wrong")

    if len(Msg) == 0:
        return render(request, 'user/dashboard.html')
    else:
        return render(request, 'user/login.html',{'Mg':Msg})


def signuph(request):

    return render(request,'user/signupadmin.html')
#####################################################
def admindashboard(request):

    # Msg=[]
    # email = request.POST.get('email')
    # password=request.POST.get('password')
    # em = myadmin.objects.filter(email=email,pw=password)
    # if em.password != password :
    #     Msg.append("password is wrong")
    # if em.email != email:
    #     Msg.append("you are not admin")
    # if len(Msg) == 0:
        return render(request, 'user/dashboardadmin.html')
    # else:
    #     return render(request, 'user/login.html',{'Mg':Msg})
#####################################################
def admindashboardh(request):

    Msg=[]
    serial = request.POST.get('serial')
    email = request.POST.get('email')
    password=request.POST.get('password')
    ser=hamayesh1.objects.filter(email=email,pw=password,serial=serial)
    if len(ser)==0:
        Msg.append("the password or serial is wrong")

    if len(Msg) == 0:
        return render(request, 'user/dashboardadminh.html')
    else:
        return render(request, 'user/login.html',{'Mg':Msg})
#####################################################
def test(request):
    return render(request,'user/test.html')
#####################################################
#####################################################
def edituserh(request,email):

    m=myuserh.objects.filter(email=email)
    return render(request,'user/signuph.html',{'k':m[0]})
#######################################################
def editadmin(request,email):

    m=myuser.objects.filter(email=email)
    return render(request,'user/signupadmin.html',{'k':m[0]})

