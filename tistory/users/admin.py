from django.contrib import admin

from .models import User #모델에 있는 유저를 가져오기

# Register your models here.

admin.site.register(User) #어드민사이트에 추가하기
