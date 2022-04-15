from pickle import TRUE
from django.db import models

# Create your models here.
# makemigrations - create changes and store in file
# migrate - apply the pending changes created by makemigrations

class Problem(models.Model):
    pid = models.BigIntegerField(primary_key=TRUE)
    p_name = models.CharField(max_length= 200)
    p_link = models.CharField(max_length= 200)
    p_input = models.CharField(max_length= 200)
    p_output = models.CharField(max_length= 200)
    p_submitted = models.CharField(max_length= 200)
    p_accepted = models.IntegerField()
    p_level = models.CharField(max_length= 10)
    p_editorial = models.CharField(max_length= 100)
    p_last_login = models.DateField()

    def __str__(self):
        return self.pid

class User_attempt(models.Model):
    sid = models.BigIntegerField()
    attempt_id = models.BigIntegerField()
    attempt_pid = models.BigIntegerField()
    attempt_username = models.BigIntegerField()
    attempt_datetime = models.DateField() 
    attempt_verdict = models.BooleanField(default= False)

    def __str__(self):
        return self.attempt_username + self.attempt_id + self.attempt_pid
