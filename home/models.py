from django.db import models


class Subscription(models.Model):
    class Meta:
        unique_together = (('userid', 'category'),)
    userid = models.IntegerField()
    category = models.CharField(max_length=20)
