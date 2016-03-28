from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LocationViewSet
from .views import FlatViewSet
from .views import RoomViewSet
from .views import EmployeeViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'flats', FlatViewSet)
router.register(r'rooms', RoomViewSet)

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]