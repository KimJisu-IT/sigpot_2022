from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.views import View

# 게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    menu1= models.CharField(max_length=200) # 한식
    menu2= models.CharField(max_length=200) # 중식
    menu3= models.CharField(max_length=200) # 일식
    menu4= models.CharField(max_length=200) # 양식
    menu5= models.CharField(max_length=200) # 분식
    menu6= models.CharField(max_length=200) # 디저트

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Check(models.Model):
    menu= models.CharField(max_length=200)
    meal_time= models.CharField(max_length=200)


