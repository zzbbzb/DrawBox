from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DrawBox(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    use_count = models.CharField(max_length=999)
    last_update = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, related_name='drawboxes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DrawGrid(models.Model):
    context = models.TextField(max_length=3000)
    weight = models.IntegerField()
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    drawbox = models.ForeignKey(DrawBox, related_name='drawgirds', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='drawgirds', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)



