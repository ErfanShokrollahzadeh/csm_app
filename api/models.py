from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    desceiption = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
