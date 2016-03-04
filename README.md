# Consume YouTubeAPI
This is a small Application using Python/Django REST framework

Django application with a simple ORM class to work with YouTube videos.                                                             
Use following parameters:

      - YouTube video ID
      - Video Title
      - Video Description
 
Python YouTube API client to search YouTube for videos with given Channel ID.

Example Channel ID: your channel ID

      - API Docs: https://developers.google.com/youtube/v3/docs/search/list
      - API Client: https://pypi.python.org/pypi/google-api-python-client/
      
      If you pass the channel ID as filter without any search query you will get all the videos in channel with a paginated result.
 
Django Rest Framework to create a couple of API endpoint to list the YouTube videos.

      - GET request to list all videos
      - GET request to get video details based on ID
