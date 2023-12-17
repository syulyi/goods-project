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
    # title = models.CharField(max_length=200)
    # category = models.TextField()
    subject = models.CharField(max_length=200, default='Default Subject')
    content = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField()

# 12-15
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name