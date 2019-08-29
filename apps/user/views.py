from django.shortcuts import render
from rest_framework import mixins, viewsets, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.


class UserLoginAPIView(views.APIView):
    # permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        # 输出当前登录用户
        print(self.request.user)
        username = data.get('username')
        password = data.get('password')
        user = User.objects.get(username__iexact=username)
        if user.check_password(password):
            serializer = UserLoginSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                new_data = serializer.data
                # 记忆已登录用户
                self.request.user = user.id
                return Response(new_data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response('password error', HTTP_400_BAD_REQUEST)


class UserLoginAPIView(views.APIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def post(self, request, *args, **kwargs):
        print(1)
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = UserProfile.objects.filter(
            username=username, password=password).first()
        print(user)
        if user and password == user.password:
            token = Token.objects.get_or_create(user=user)
            print(token)
            return Response(status=status.HTTP_200_OK, data={'msg': '登录成功'})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'msg': '登录失败'})


class UserRegisterAPIView(views.APIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = UserProfile.objects.filter(username=username).first()
        if not user:
            UserProfile.objects.create_user(
                username=username, password=password)
            return Response(status=status.HTTP_200_OK, data={'msg': '注册成功'})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'msg': '用户名已被占用'})
