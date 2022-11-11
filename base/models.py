from django.db import models

# Create your models here.
class TodoUser(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False) # field required
    description = models.TextField(blank=True, null=True) # not required
    user_avatar = models.ImageField(upload_to='users_avater', blank=True, default='no_pic.jpg')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    user = models.ForeignKey(TodoUser, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=300) # field required
    task_description = models.TextField() # field not required
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}: {self.task_name}'
    