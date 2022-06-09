from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #null True: it is allowed to be blank
    #participants = 
    updated = models.DateTimeField(auto_now=True) #timestamp every time
    created = models.DateTimeField(auto_now_add=True) #timestamp when created

    def __str__(self):
        return self.name

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #if parent deleted, delete children
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #timestamp every time
    created = models.DateTimeField(auto_now_add=True) #timestamp when created

    def __str__(self):
        return self.body[:50]