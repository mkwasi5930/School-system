from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', include('admin.urls', namespace='admin')),
    path('students/', include('students.urls', namespace='students')),
]
