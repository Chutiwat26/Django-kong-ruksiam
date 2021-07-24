from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!!")

#ทำการ reder หน้าเว็ปแทนการ response
#การ render สามารถส่งข้อมูลไปให้ templates ได้โดยใช้ json format
def show_index(request):
    tags=['กุ้ง','ปู','ปลา']
    rating=10
    return render(request,'index.html',{'name':'รายการสินค้าจับจ่าย',
    'author':'chutiwat tanapibalwongsa',
    'tags':tags,
    'rating':rating})

def page1(request):
    return render(request,'page1.html')