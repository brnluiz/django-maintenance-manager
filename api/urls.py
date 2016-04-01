from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LocationViewSet
from .views import FlatViewSet
from .views import RoomViewSet
from .views import StaffViewSet
from .views import ResidentViewSet
from .views import EnquireViewSet
from .views import ReportViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'flats', FlatViewSet)
router.register(r'rooms', RoomViewSet)

router.register(r'residents', ResidentViewSet)

router.register(r'staff', StaffViewSet)
router.register(r'enquires', EnquireViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]