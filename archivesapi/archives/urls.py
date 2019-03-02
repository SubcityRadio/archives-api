from django.urls import path
from .apiviews import ArchiveYearList, ArchivePostYearDetailList
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path("years/", ArchiveYearList.as_view(), name="archive_year_list"),
    path("year/<int:pk>/", ArchivePostYearDetailList.as_view(), name="archive_post_year_detail"),
    # path("favicon.ico", RedirectView.as_view( url=staticfiles_storage.url('favicon.ico'), permanent=False), name="favicon")
]