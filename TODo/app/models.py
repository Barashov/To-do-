from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Affairs(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Affair"
        verbose_name_plural = "Affairs"

    def __str__(self):
        return self.name


