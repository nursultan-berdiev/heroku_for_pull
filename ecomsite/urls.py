from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryViewSet, ItemViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('item', ItemViewSet, basename='item')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('get-token/', obtain_auth_token),
]
