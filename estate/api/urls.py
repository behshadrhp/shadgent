from estate.api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('estate', views.EstateViewSet, basename='estate')


urlpatterns = router.urls
