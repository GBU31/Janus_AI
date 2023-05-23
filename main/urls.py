from django.urls import path, include
from rest_framework import routers
from .views import *
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'api', MyModelViewSet)

urlpatterns = [ path('', index),
    path('api',  MyModelViewSet.as_view({'post': 'upload_file'}), name='upload_file'),
]