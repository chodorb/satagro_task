from rest_framework import serializers
from techlines.models import TechLine

class TechlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechLine
        fields = '__all__'