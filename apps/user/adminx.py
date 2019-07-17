import xadmin

from .models import AuthorProfile, UserProfile


class AuthorProfileAdmin(object):
    list_display = ['username', 'age', 'phone', 'email', 'gender', 'avater']

class UserProfileAdmin(object):
    list_display = ['username', 'age', 'phone', 'email', 'gender', 'avater']


xadmin.site.register(AuthorProfile, AuthorProfileAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)
