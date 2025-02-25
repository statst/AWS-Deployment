from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo