from django.contrib import admin
from django.urls import include, path  # test3

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
