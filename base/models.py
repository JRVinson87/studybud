from django.db import models

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

    
