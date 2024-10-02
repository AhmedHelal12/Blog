from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField(null=False)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateField(auto_now_add=True)

