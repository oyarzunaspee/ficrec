from django.db import models
from django.conf import settings

class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=300)
    about = models.TextField(null=True)

    def __str__(self):
        return self.name
    
class Rec(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    word_count = models.PositiveIntegerField()
    summary = models.TextField()
    notes = models.TextField(null=True)
    url = models.URLField(max_length=42)

    def __str__(self):
        return self.title