from django.db import models
# For foreignKey
class Post(models.model):
    author = models.ForeignKey('auth.User' , on_delete=models.CASCADE, related_name='posts')


#OneToOne Field - 
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User',on_delete= models.CASCADE,related_name='Profile')
    bio = models.TextField()


#ManyToManyField  
class Course(models.Model):
    Student = models.ManyToManyField('auth.User',related_name='Courses', blank= True)