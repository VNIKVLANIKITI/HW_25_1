from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('education.urls', namespace='educations')),
    path('users/', include('users.urls', namespace='users')),
]
