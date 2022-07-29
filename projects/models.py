from django.db import models
from accounts .models import Account

# Create your models here.

class Status(models.Model):
    title       = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Main Project Model
class Project(models.Model):
    title       = models.CharField(max_length=255)
    desc        = models.TextField(max_length=10000)
    company     = models.ForeignKey(Account, on_delete=models.CASCADE)
    deadline    = models.CharField(max_length=255)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Project Part Model
class Part(models.Model):
    title       = models.CharField(max_length=255)
    project     = models.ForeignKey(Project, on_delete=models.CASCADE)
    desc        = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Part Comment Model
class Comment_Part(models.Model):
    client      = models.ForeignKey(Account, on_delete=models.CASCADE)
    pr_part     = models.ForeignKey(Part, on_delete=models.CASCADE)
    comment     = models.TextField()

    def __str__(self):
        return self.pr_part.title

# Todo Status Model
class Td_status(models.Model):
    status      = models.CharField(max_length=255)

    def __str__(self):
        return self.status

# Part Todo Model
class Todo(models.Model):
    pr_part     = models.ForeignKey(Part, on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    desc        = models.TextField(blank=True, null=True)
    status      = models.ForeignKey(Td_status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title