from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=20)
    role=models.TextField()
    facebook=models.TextField(null=True,blank=True)
    image=models.ImageField(null=False,upload_to="team/team_members/" )
    
    def __str__(self):
        return self.name

class Messages(models.Model):
    name=models.CharField(max_length=20)
    message=models.TextField()
    senderemail=models.EmailField()
     
    def __str__(self):
        return self.name+' '+'('+self.senderemail+') '+'" '+self.message+' "'
 
class Blogs(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=150)
    blog=models.TextField()
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to="blogs/")
    postedby=models.CharField(max_length=25)
    createdat=models.TimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title