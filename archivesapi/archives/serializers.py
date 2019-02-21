from rest_framework import serializers

from .models import ArchivePost, ArchiveYear


class ArchivePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivePost
        fields = '__all__'

class ArchiveYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveYear
        fields = ['year']