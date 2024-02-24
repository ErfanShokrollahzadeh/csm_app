from asyncio import AbstractServer
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(
        'username',
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    password = models.CharField(
        'password',
        max_length=128,
        help_text='A raw password representing the user’s password.',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'


class Onbording(models.Model):
    title = models.CharField(max_length=200)
    discriptions = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Onbording info'
