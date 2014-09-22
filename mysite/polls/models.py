from django.db import models

class Poll(models.Model):
  question = models.CharField(max_length=300)
  pub_date = models.DateTimeField(verbose_name='Date published')

  def __unicode__(self):
    return self.question

  class Meta:
    #fields = ['question', 'pub_date']
    pass

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)