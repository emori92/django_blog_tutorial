from django.db import models


# Create your models here.
class Blog(models.Model):
    
    class Meta:
        db_table = 'Blog'

    title = models.CharField(max_length = 150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.title
