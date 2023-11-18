from django.db import models

# Create your models here.


class ImapCredentials(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    server = models.CharField(max_length=200)
    port = models.IntegerField(default=993)
    ssl = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)
