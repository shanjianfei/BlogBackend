import xadmin

from .models import AuthorProfile, UserProfile


class AuthorProfileAdmin(object):
    list_display = ['username', 'age', 'phone', 'email', 'gender', 'avater', 'active']

class UserProfileAdmin(object):
    list_display = ['username', 'age', 'phone', 'email', 'gender', 'avater', 'active']


xadmin.site.register(AuthorProfile, AuthorProfileAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)
