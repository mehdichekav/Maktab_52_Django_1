from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
    # prefix_default_language=True
)
