from django.db import models
import random
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(
                blank=True,
                null=True)
    image = models.FileField(
                upload_to="images/",
                blank=True,
                null=True)



    class Meta:
        ordering = ['-id']
    def __str__(self):
        return str(self.content)
    
    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes":random.randint(0,200)
        }