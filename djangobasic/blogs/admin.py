from django.contrib import admin
from .models import Post

# Register your models here.
# กำหนด model ให้ admin มองเห็น

admin.site.register(Post)