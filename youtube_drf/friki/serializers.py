from rest_framework import serializers
from friki.models import YouTube

class YouTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTube
        fields = ('id', 'title', 'description')


