from rest_framework import serializers

from .models import Bboy, Crew, City

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class BboySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bboy
        fields = '__all__'
