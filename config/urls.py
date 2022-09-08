
from django.contrib import admin
from django.urls import path, include
from candidates.presidency.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += router.urls