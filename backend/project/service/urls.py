from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'plan', views.PlanViewSet)
router.register(r'work', views.WorkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
