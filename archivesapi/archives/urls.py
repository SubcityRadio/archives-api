from django.urls import path
from .apiviews import ArchiveYearList, ArchivePostYearDetailList

urlpatterns = [
    path("years/", ArchiveYearList.as_view(), name="archive_year_list"),
    path("year/<int:pk>/", ArchivePostYearDetailList.as_view(), name="archive_post_year_detail")
]