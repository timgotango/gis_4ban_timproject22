from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,    # user 탈퇴하면 구독 정보도 삭제
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)
    class Meta:
        unique_together = ['user', 'project']    # user와 project 쌍으로 묶어주기!