from django.urls import path
from video_api.views import VideoList, VideoPrice, VideoUpload


urlpatterns = [
    path("videos/list/", VideoList.as_view(), name="video_list"),
    path("videos/upload/", VideoUpload.as_view(), name="video_upload"),
    path("videos/cost/", VideoPrice.as_view(), name="video_cost"),
]
