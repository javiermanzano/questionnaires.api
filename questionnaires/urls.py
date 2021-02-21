from django.urls import include, path
from rest_framework import routers
from questionnaires import views

router = routers.DefaultRouter()
router.register(r'collected-data', views.CollectedDataViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
