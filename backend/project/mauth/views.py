# Create your views here.
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .permissions import IsCurrentUserOrReadOnly
from .models import Profile
from project.mauth.serializers import MyUserSerializer, ProfileSerializer


class UserCreate(APIView):
    serializer_class = MyUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                payload = jwt_payload_handler(user)
                json['token'] = jwt_encode_handler(payload)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOrReadOnly)
