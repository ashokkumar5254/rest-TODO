from django.db import models

# Create your models here.
class todo_model(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    Date=models.DateField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    def __str__(self):
        return self.Title
