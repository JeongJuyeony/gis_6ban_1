from django.db import models


# Create your models here.

# 새로운 DB 객체를 만들기 위해 클래스 선언 (models.Model 에서 상속)
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

