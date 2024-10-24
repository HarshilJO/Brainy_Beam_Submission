# urls.py
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Create a router and register the PostViewSet with it
# router = DefaultRouter()
# router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostViewSet.as_view())
    # path('api/', include(router.urls)),  # Include the router's URLs for posts
]
