from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    