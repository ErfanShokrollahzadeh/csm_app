from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=200)
    desceiption = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name='todos', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
