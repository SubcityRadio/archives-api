from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import ArchivePost, ArchiveYear
from .serializers import ArchivePostSerializer, ArchiveYearSerializer

class ArchiveYearList(APIView):
    def get(self, request):
        all_archive_years = ArchiveYear.objects.distinct('year')
        data = ArchiveYearSerializer(all_archive_years, many=True).data
        return Response(data)


class ArchivePostYearDetailList(APIView):
    def get(self, request, pk):
        year_posts = ArchivePost.objects.filter(year=pk)
        data = ArchivePostSerializer(year_posts, many=True).data
        return Response(data)