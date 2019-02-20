from django.urls import path
from .views import archive_post_year_list, archive_post_year_detail

urlpatterns = [
    path("year/", archive_post_year_list, name="archive_post_year_list"),
    path("year/<int:pk>/", archive_post_year_detail, name="archive_post_year_detail")
]
