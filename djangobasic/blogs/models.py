from django.db import models

# Create your models here.
#class Post เปรียบเสมือนการสร้างตาราง Post
class Post(models.Model):
    #เปรียบเสมือนการสร้าง column
    name=models.CharField(max_length=200)
    description=models.TextField()