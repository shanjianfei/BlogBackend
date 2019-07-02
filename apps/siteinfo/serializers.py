from rest_framework import serializers
from .models import SiteInfoModel


class SiteInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfoModel
        fields = ('logo', 'motto', 'filing', 'copyright', 'open_source_license', 'url_osl')
