from rest_framework import serializers
from .models import Route
from complaints.serializers import ComplaintSerializer

class RouteSerializer(serializers.ModelSerializer):
    complaints = ComplaintSerializer(many=True, read_only=True, source='complaint_set')

    class Meta:
        model = Route
        fields = '__all__'