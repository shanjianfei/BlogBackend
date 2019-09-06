from rest_framework import mixins, status, views
from rest_framework.response import Response
from .models import UserProfile
from rest_framework.authtoken.models import Token

# Create your views here.


class UserLoginAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = UserProfile.objects.filter(
            username=username).first()
        if user and user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            user_info = {
                'user': user.username,
                'token': token[0].key
            }
            return Response(status=status.HTTP_200_OK, data={'msg': '登录成功', 'user_info': user_info})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'msg': '登录失败'})


class UserRegisterAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = UserProfile.objects.filter(username=username).first()
        if not user:
            user_new = UserProfile.objects.create_user(
                username=username, password=password)
            Token.objects.create(user=user_new)
            return Response(status=status.HTTP_200_OK, data={'msg': '注册成功'})
        return Response(status=status.HTTP_409_CONFLICT, data={'msg': '用户名已被占用'})
