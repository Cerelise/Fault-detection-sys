from rest_framework import serializers
from .models import TrainsUpload,TestsUpload


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsUpload
        fields = '__all__'

class TrainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainsUpload
        fields = '__all__'

class MultipleTrainsSerializer(serializers.Serializer):
    trains = serializers.ListField(
      child=serializers.FileField()
    )


