from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=40)
    note = models.TextField()
    
    def __str__(self):
        return self.title