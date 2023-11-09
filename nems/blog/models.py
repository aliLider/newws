from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField("Nomi", max_length=255)
    image = models.ImageField("rasm", blank=True, null=True)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriya"

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Sarlavhasi', max_length=225)
    image = models.ImageField('Rasm', blank=True, null=True)
    content = models.TextField('Yangilik haqida')
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    views = models.IntegerField("Ko'rilganlar", default=0)
    date = models.DateTimeField("Sana", default=timezone.now)
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_text = models.TextField("Kommentariya", max_length=1000)

    class Meta:
        verbose_name = "Kommentariya"
        verbose_name_plural = "Kommentariya"
    
    def __str__(self):
        return self.comment_text



