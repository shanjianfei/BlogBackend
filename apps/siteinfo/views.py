from rest_framework import viewsets
from .models import SiteInfoModel
from .serializers import SiteInfoModelSerializer

# Create your views here.


class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = SiteInfoModel.objects.all()
    serializer_class = SiteInfoModelSerializer
