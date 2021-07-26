from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 장고에서 제공해주는 models.Model을 상속받음
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # on_delete=models.CASCADE : account가 사라지면 연결되어있는 profile도 삭제하겠다. account : profile = 1:1
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)

