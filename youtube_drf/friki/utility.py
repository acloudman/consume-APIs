#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from friki.models import YouTube

try:
	API_KEY = settings.YOUTUBE_API_KEY
	SERVICE_NAME = settings.YOUTUBE_API_SERVICE_NAME
	API_VERSION = settings.YOUTUBE_API_VERSION
except Exception, e:
	raise NotImplementedError(str(e))

youtube = build(SERVICE_NAME, API_VERSION, developerKey=API_KEY)
part = "snippet"
# channelId = 'UCMDV6J2hWXet7ZCfgrXGgeg'

class GetVideos(object):
	query_result = []
	def __init__(self, channelId):
		self.channelId = channelId

	def next_page(self,pageToken):
	    search_response = youtube.search().list(part=part,channelId=self.channelId,pageToken=pageToken,).execute()
	    for i in range(len(search_response['items'])):
	        self.query_result.append(search_response['items'][i])
	    response = self.check_next_page(search_response)
	    return search_response

	def check_next_page(self,result):
	    if "nextPageToken" in result:
	        pageToken = result['nextPageToken']
	        result = self.next_page(pageToken)
	    return result

	def youtube_search(self):
	    search_response = youtube.search().list(part=part,channelId=self.channelId,).execute()
	    for i in range(len(search_response['items'])):
	        self.query_result.append(search_response['items'][i])
	    search_response  = self.check_next_page(search_response)
	    for result in self.query_result:
	        b, created = YouTube.objects.get_or_create(
			title = result['snippet']['title'],
			description = result['snippet']['description']
			)

if __name__ == "__main__":
    try:
        YouTubeVideos()
        # create_data()
    except HttpError, e:
        print e
