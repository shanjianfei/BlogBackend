from rest_framework import serializers
from .models import BaseCategory, BlogCategory, Tags, BaseBlog
from article.models import Article


class CategoryLevel1ListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(category_level=1)
        return super().to_representation(data)


class CategoryLevelSerializer3(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class CategoryLevelSerializer2(serializers.ModelSerializer):
    sub_categorylevel = CategoryLevelSerializer3(many=True)

    class Meta:
        model = BlogCategory
        fields = '__all__'


class CategoryLevelSerializer(serializers.ModelSerializer):
    sub_categorylevel = CategoryLevelSerializer2(many=True)

    class Meta:
        list_serializer_class = CategoryLevel1ListSerializer
        model = BlogCategory
        fields = '__all__'


class BaseCategorySerializer(serializers.ModelSerializer):
    sub_category = CategoryLevelSerializer(many=True)

    class Meta:
        model = BaseCategory
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


class BaseBlogReadPermissionVerificationSerializer(serializers.Serializer):
    blog_id = serializers.IntegerField()
    password = serializers.CharField(max_length=10, min_length=4)
