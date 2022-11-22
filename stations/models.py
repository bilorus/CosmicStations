from django.conf import settings
from django.db import models


class Station(models.Model):
    StationCondition = models.TextChoices('StationCondition', 'RUNNING BROKEN')

    name = models.CharField(max_length=150)
    axis_x = models.IntegerField(default=100)
    axis_y = models.IntegerField(default=100)
    axis_z = models.IntegerField(default=100)
    condition = models.CharField(choices=StationCondition.choices, max_length=10, default='RUNNING', editable=False)
    time_create = models.DateTimeField(auto_now_add=True, editable=False)
    time_broke = models.DateTimeField(editable=False, null=True)

    def __str__(self):
        return self.name


class Indication(models.Model):
    AxisChoices = models.TextChoices('AxisChoices', 'X Y Z')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    axis = models.CharField(choices=AxisChoices.choices, max_length=6)
    distance = models.IntegerField()
