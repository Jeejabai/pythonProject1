from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse


def form(request):
    return render(request,'reg.html')
def show(request):
   if request.method == "POST":
       name = request.POST['name']
       phone = request.POST['mobile']
       address = request.POST['address']
       email = request.POST['email']
       password = request.POST['password']
       a=Form(name=name,mobile=phone,address=address,email=email,password=password)
       a.save()
       b=Login(email=email,password=password,type=1)
       b.save()
       return redirect(log)
def read(request):
    j=Form.objects.all()
    z={'re':j}
    return render(request,'login.html',z)
def log(request):
    return render(request,'login.html')
def valid(request):
    email=request.POST['email']
    password=request.POST['password']
    c=Login.objects.get(email=email,password=password)
    if c.type==1:
        request.session['email'] = c.email
        return redirect(user)
    elif c.type==2:
        request.session['email'] = c.email
        return redirect(jee)
    elif c.type==0:
        request.session['email'] = c.email
        return redirect(super)

def user(request):
    if 'email' in request.session:
        ab = Product.objects.all()
        p = {
            'pop': ab
        }
        return render(request, 'user.html', p)

    return redirect("/")


def jee(request):
    if 'email' in request.session:
        cd = Product.objects.all()
        q = {
            'lock': cd
        }
        return render(request, 'admin.html', q)
    return redirect("/")


def super(request):
    if 'email' in request.session:
        ef = Product.objects.all()
        r = {
            'star': ef
        }
        return render(request, 'super.html', r)


    return redirect("/")
def pro(request):
    return render(request, 'pro.html')
def product(request):
    if request.method=="POST":
        number = request.POST['number']
        type = request.POST['type']
        model = request.POST['model']
        des = request.POST['des']
        img = request.FILES['img']
        jee=Product(number=number,type=type,model=model,des=des,img=img)
        jee.save()
    return render(request,'pro.html')
def edit(request,id):
    if request.method == "POST":
        number = request.POST['number']
        type = request.POST['type']
        model = request.POST['model']
        des = request.POST['des']
        img = request.FILES['img']
        left=Product.objects.get(id=id)
        left.number = number
        left.type = type
        left.model = model
        left.des = des
        left.img = img
        left.save()
        return redirect(jee)
    d=Product.objects.get(id=id)
    do={
        'put':d
    }
    return render(request,'proedit.html',do)
def delete(request,id):
    hlo=Product.objects.get(id=id)
    hlo.delete()
    return redirect(super)

def logout(request):
    if 'email' in request.session:
        request. session.flush()
    return redirect(log)
