from django.db import models
class ClientMark(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=255)
    rank = models.IntegerField()