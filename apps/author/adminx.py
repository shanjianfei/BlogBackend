from .models import AuthorModel

import xadmin


class AuthorModelAdmin(object):
    list_display = ['name', 'age', 'phone', 'email', 'gender', 'avater']


xadmin.site.register(AuthorModel, AuthorModelAdmin)
