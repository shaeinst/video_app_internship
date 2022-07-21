from rest_framework import serializers
from video_api.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "title", "created", "upload"]


class CostSerializer(serializers.Serializer):
    type = serializers.CharField()
    duration = serializers.IntegerField()
    size = serializers.FloatField()
