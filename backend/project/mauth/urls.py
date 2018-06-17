from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from project.mauth import views
from .views import UserCreate

router = DefaultRouter()
router.register('profiles', views.ProfileViewSet)

urlpatterns = [
    path('sign-in', obtain_jwt_token),
    path('sign-up', UserCreate.as_view()),
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]