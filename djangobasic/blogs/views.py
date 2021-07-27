from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
#บันทึกข้อมูลลงไปใน model user ต้อง import User เข้ามาก่อน
from django.contrib.auth.models import User, auth
#import library สำหรับแสดงข้อความแจ้งเตือน
from django.contrib import messages

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!!")

#ทำการ reder หน้าเว็ปแทนการ response
#การ render สามารถส่งข้อมูลไปให้ templates ได้โดยใช้ json format
def show_index(request):
    #tags=['กุ้ง','ปู','ปลา']
    #rating=10
    #return render(request,'index.html',{'name':'รายการสินค้าจับจ่าย','author':'chutiwat tanapibalwongsa','tags':tags,'rating':rating})

    #Query data from model
    data = Post.objects.all()
    return render(request,'index.html',{'posts':data})

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request, 'form.html')

def loginform(request):
    return render(request, 'login.html')

def addForm(request):
    #รับข้อมูลจาก tag field ในไฟล์ html โดยอ้างอิงจากชื่อของ tag field นั้นๆ
    #name = request.GET['name']
    #description = request.GET['description']
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    # key ใน User.objects.create_user คือชื่อ field ใน table auth_user
    if password == repassword:
        if User.objects.filter(username=username).exists:
            #แสดงข้อความแจ้งเตือน
            messages.info(request,'Username is exist.')
            #print("Username is exist.")
            return redirect('/createForm')
        elif User.objects.filter(email = email).exists:
            messages.info(request,'This email is in used.')
            #print("This email is in used.")
            return redirect('/createForm')
        else:
            user = User.objects.create_user(username=username, password=password, email=email,first_name=fname,last_name=lname)
            user.save()
            return redirect('/')
            #return render(request, 'result.html')
    else:
        messages.info(request,'Password not match.')
        #print("Password not match.")
        return redirect('/createForm')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #เช็ค username กับ password ว่าตรงกันในฐานข้อมูลหรือป่าว
    user = auth.authenticate(username=username, password=password)
    #ถ้า username กับ password ถูกต้อง user is not none.
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginform')

def logOut(request):
    auth.logout(request)
    return redirect('/')


