from django.db import models


class Record(models.Model):
    type = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
