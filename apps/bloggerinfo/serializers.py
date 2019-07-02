from rest_framework import serializers
from .models import Social, BloggerInfo


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('name','desc','url','image','image_height','image_width')

class BloggerInfoSerializer(serializers.ModelSerializer):
    social = SocialSerializer(many=True)
    class Meta:
        model = BloggerInfo
        fields = ('name_zh', 'name_en', 'intro', 'email', 'phone_number', 'avatar', 'background', 'social')