from rest_framework import serializers
from .models import BlogCategory, Tags, BaseBlog
from article.models import Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class CategorySerializer2(serializers.ModelSerializer):
    sub_category = CategorySerializer(many=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'

class CategorySerializer3(serializers.ModelSerializer):
    sub_category = CategorySerializer2(many=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    article_count = serializers.SerializerMethodField()

    def get_article_count(self, instance):
        # return Article.objects.filter(tags=instance).count()
        # return instance.article_set.all().count() # 多对多不行
        return instance.blog.all().count()  # 利用related_name 反查询

    class Meta:
        model = Tags
        fields = '__all__'


class BaseBlogSerialzier(serializers.ModelSerializer):

    class Meta:
        model = BaseBlog
        fields = '__all__'
