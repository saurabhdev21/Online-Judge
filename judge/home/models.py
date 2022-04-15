import datetime
from pickle import TRUE
from django.db import models

from judge.settings import BASE_DIR, PROBLEMS, PROBLEMS_INPUT, PROBLEMS_OUTPUT, STATIC_URL

# Create your models here.
# makemigrations - create changes and store in file
# migrate - apply the pending changes created by makemigrations


class Problems(models.Model):
    pid = models.IntegerField(primary_key=TRUE)
    p_name = models.CharField(max_length= 200)
    p_link = models.FilePathField(path = BASE_DIR/STATIC_URL/PROBLEMS)
    p_input = models.FilePathField(path = BASE_DIR/STATIC_URL/PROBLEMS_INPUT)
    p_output = models.FilePathField(path = BASE_DIR/STATIC_URL/PROBLEMS_OUTPUT)
    p_submitted = models.CharField(max_length= 200)
    p_accepted = models.IntegerField()
    p_level = models.CharField(max_length= 10)
    p_editorial = models.CharField(max_length= 100)
    # p_last_login = models.DateField(null=TRUE, blank=TRUE, default= datetime.date.today())

    def __str__(self):
        return self.pid


class User_attempt(models.Model):
    sid = models.IntegerField(default=1)
    attempt_id = models.IntegerField(default=1)
    attempt_pid = models.IntegerField(default=1)
    attempt_username = models.IntegerField(default='')
    # attempt_datetime = models.DateField(null=TRUE, blank=TRUE, default= datetime.date.today()) 
    attempt_verdict = models.BooleanField(default= False)

    def __str__(self):
        return self.attempt_username + self.attempt_id + self.attempt_pid
