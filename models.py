from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)  # 标题
    body = models.TextField()  # 内容
    created_time = models.DateTimeField() #创建时间
    modified_time = models.DateTimeField() # 更新时间
    excerpt = models.CharField(max_length=200, blank=True) # 摘要
    category = models.ForeignKey(Category) # 分类
    tags = models.ManyToManyField(Tag, blank=True) # 标签
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
