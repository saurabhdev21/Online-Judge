from django.db import models

# Create your models here.
# makemigrations - create changes and store in file
# migrate - apply the pending changes created by makemigrations

class Problem(models.Model):
    pid = models.BigIntegerField()
    email = models.CharField(max_length= 122)
    phone = models.CharField(max_length= 13)
    suggestions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.pid

class Submission(models.Model):
    sid = models.BigIntegerField()