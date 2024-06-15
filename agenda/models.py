from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# from django.conf import settings



# def CustomUser(AbstractUser):
#   first_name = models.CharField(max_length=200, null=True)
#   last_name = models.CharField(max_length=200, null=True)
#   email = models.EmailField(unique=True, null=True)
#   username = models.CharField(unique=True, null=True)

#   def __str__(self):
#         return self.username




class SharedList(models.Model):
    name = models.CharField(max_length=100, default='Bucket List')
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_lists_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_lists_user2')

    def __str__(self):
        return f"{self.user1.username} & {self.user2.username} - {self.list.name}"

  

class Task(models.Model):
    shared_list = models.ForeignKey(SharedList, on_delete=models.CASCADE, related_name='tasks')
    list_type = models.CharField(max_length=100) #bucket list or todo
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    planned_date = models.DateTimeField(null=True)
    planned_time = models.DateTimeField(null=True)
    planned_location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

