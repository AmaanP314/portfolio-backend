# # api/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProjectViewSet, BlogPostViewSet

# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet)
# router.register(r'blogposts', BlogPostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from django.urls import path
# from .views import HelloWorldView

# urlpatterns = [
#     path('hello/', HelloWorldView.as_view(), name='hello_world'),
# ]

from django.urls import path
from .views import send_email

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
]

