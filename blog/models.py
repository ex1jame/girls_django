# from django.db import models


from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#
#
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = 'People'
#         verbose_name = 'Person'
#
#     def __str__(self):
#         return self.name
#
# class Cat(models.Model):
#     color = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     mood = models.CharField(max_length=255)
#     owner = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="people", null=True, blank=True)
#     age = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = 'Cats'
#         verbose_name = 'Cat'
#
#     def __str__(self):
#         return self.name
#
#     def purr(self):
#         return f'{self.name} мурчит'
#
#     def scratch(self):
#         return f'{self.name} царапаеться'
#
#     def feed(self):
#         return f'{self.name} покормили {CatFood.food}со вкусом {CatFood.taste}'
#
# class CatFood(models.Model):
#     food = models.CharField(max_length=255)
#     taste = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name_plural = 'Кошачья Еда'
#         verbose_name = 'Еда'
#
#     def __str__(self):
#         return self.food
#
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     text = models.TextField(max_length=255)
#     author = models.ForeignKey(Person,related_name="people", blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True, blank=True)
#     published_date = models.DateTimeField(auto_now=True, blank=True)
#
#     class Meta:
#         verbose_name_plural = 'Posts'
#         verbose_name = 'Post'
#
#     def __str__(self):
#         return self.title