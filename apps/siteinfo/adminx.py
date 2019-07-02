from .models import SiteInfoModel
import xadmin


class SiteInfoModelAdmin(object):
    list_display = ('logo', 'motto', 'filing', 'copyright', 'open_source_license', 'url_osl')


xadmin.site.register(SiteInfoModel, SiteInfoModelAdmin)
