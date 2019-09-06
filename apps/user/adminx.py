import xadmin

from .models import UserProfile


# class AuthorProfileAdmin(object):
#     list_display = ['username', 'age', 'phone',
#                     'email', 'gender', 'avater', 'active']
#     readonly_fields = ('create_time',)

#     class Meta:
#         fields = ['username', 'age', 'phone',
#                     'email', 'gender', 'avater', 'active']


# class UserProfileAdmin(object):
#     list_display = ('username', 'first_name', 'last_name', 'email',
#                     'is_staff', 'is_active', 'date_joined', 'last_login')
#     readonly_fields = ('date_joined', 'last_login_time')


# xadmin.site.register(AuthorProfile, AuthorProfileAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)
