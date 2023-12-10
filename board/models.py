from django.db import models

# Create your models here.

# ------------------------
# Board 모델(테이블)은
# ------------------------
# 제목(title),
# 카테고리(category) 그리고
# 작성일시(create_date)를 구성
# ------------------------

class Board(models.Model):
    title = models.CharField(max_length=200)
    category = models.TextField()
    create_date = models.DateTimeField()
