from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ArchivePost

def archive_post_year_list(request):
    year_list = ArchivePost.objects.all()
    data = {"results": list(year_list.values("year"))}
    return JsonResponse(data)

def archive_post_year_detail(request, pk):
    year_posts = ArchivePost.objects.filter(year=pk)
    data = {"results": list(year_posts.values("title", "year", "post_content", "post_summary", "post_image_alt_text"))}
    return JsonResponse(data)