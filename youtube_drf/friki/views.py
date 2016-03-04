from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from friki.models import YouTube
from friki.serializers import YouTubeSerializer


@api_view(['GET', 'POST'])
def video_list(request, format=None):
    if request.method == 'GET':
        videos = YouTube.objects.all()
        serializer = YouTubeSerializer(videos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YouTubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk, format=None):
    try:
        videos = YouTube.objects.get(pk=pk)
    except YouTube.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YouTubeSerializer(videos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = YouTubeSerializer(videos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        videos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)