from django.db import models
from django.contrib.auth.models import User
import uuid 

# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Message(models.Model):
    room = models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE)
    sender = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room.name}({self.sender.name} : {self.content})'
    
    class Meta: 
        ordering = ('created_at',)