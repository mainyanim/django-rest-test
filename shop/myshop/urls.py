from django.conf.urls import url, include
from rest_framework import routers
from .views import index, ItemsViewSet

router = routers.DefaultRouter()
router.register(r'^api', ItemsViewSet)

urlpatterns = [
    url(r'^myshop', index),
    url(r'^',include(router.urls))
]
