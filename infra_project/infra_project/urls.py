from django.contrib import admin
from django.urls import include, path  # test2

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
