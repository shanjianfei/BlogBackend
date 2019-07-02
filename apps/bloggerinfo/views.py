from rest_framework import viewsets, mixins
from .serializers import BloggerInfoSerializer
from .models import BloggerInfo

# Create your views here.

class BloggerInfoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = BloggerInfo.objects.all()
    serializer_class = BloggerInfoSerializer
