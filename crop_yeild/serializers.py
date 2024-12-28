from rest_framework import serializers
from .models import TemperatureHumidity

class TempHumiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureHumidity
        fields = ['id','timestamp' , 'temperature' , 'humidity']