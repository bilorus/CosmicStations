from rest_framework import serializers

from stations.models import Station


class StationSerializer(serializers.ModelSerializer):
    axis_x = serializers.IntegerField(default=100, initial=100)
    axis_y = serializers.IntegerField(default=100, initial=100)
    axis_z = serializers.IntegerField(default=100, initial=100)

    class Meta:
        model = Station
        fields = '__all__'
