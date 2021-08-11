from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)   # 게시글과 1대 다 연결
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)    # set_null : 삭제되면 writer 미상으로 처리
    content = models.TextField(null=False)  # 내용 있어야 하므로
    created_at = models.DateTimeField(auto_now_add=True)   # DateTimeField는 날짜 + 시간까지