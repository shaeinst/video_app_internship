from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from video_api.models import Video
from video_api.serializers import VideoSerializer, CostSerializer
from .handler import video_lenght


class VideoList(APIView):
    """
    List all Video
    """

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class VideoUpload(APIView):
    """
    upload a new Video.
    """

    def post(self, request, format=None):

        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            uploadedfile = request.FILES["upload"]

            # video sizde handling
            files_size = uploadedfile.size
            # 1GB = 1073741824 Bytes
            if files_size > 1073741824:
                err_msg = {"upload": "file size can't be more than 1GB"}
                return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)

            # video length handling
            temporary_file_path = uploadedfile.temporary_file_path()
            duration = video_lenght(temporary_file_path)

            if duration > 600:
                err_msg = {"length": "video can't be more than 600 sec (10 min)"}
                return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoPrice(APIView):
    """
    Inquiry video uploading cost
    """

    def post(self, request, format=None):
        serializer = CostSerializer(data=request.data)
        if serializer.is_valid():
            inquiry_data = serializer.data
            type = inquiry_data["type"]
            video_size = inquiry_data["size"]
            duration = inquiry_data["duration"]

            if type not in ["mkv", "mp4"]:
                return JsonResponse({"type": "we only support mp4 and mkv format"})

            if video_size > 1000:
                return JsonResponse(
                    {
                        "size": "size can't be more that 1000MB",
                    }
                )

            cost = 12.5
            if video_size <= 500:
                cost = 5.0

            additional_cost = 20.0
            # 6:18 min = 378sec
            if duration <= 378:
                additional_cost = 12.5

            cost = {
                "cost": cost + additional_cost,
            }

            return Response(cost, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
