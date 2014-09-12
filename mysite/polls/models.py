from django.db import models

class Poll(models.Model):
  question = models.CharField(max_length=300)
  pub_date = models.DateTimeField()