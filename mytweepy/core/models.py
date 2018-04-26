from django.db import models


class Account(models.Model):
    screen_name = models.CharField(max_length=50, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.twitter_handle


class Tweet(models.Model):
    account = models.ForeignKey(Account, related_name='tweets', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    added_on = models.DateTimeField(auto_now_add=True)
