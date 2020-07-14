from django.conf import global_settings
from django.db import models


class Friend(models.Model):
    name = models.CharField(max_length=100)


class OwnedModel(models.Model):
    owner = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Belonging(models.Model):
    name = models.CharField(max_length=100)


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)

    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
