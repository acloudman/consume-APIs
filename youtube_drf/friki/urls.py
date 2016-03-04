from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from friki import views

urlpatterns = [
    url(r'^videos/$', views.video_list),
    url(r'^videos/(?P<pk>[0-9]+)/$', views.video_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)