"""amdtelecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


admin.sites.AdminSite.site_header = 'Amd telecom'
admin.sites.AdminSite.site_title = 'Amd telecom'
admin.sites.AdminSite.index_title = 'Amd telecom'

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('index.urls')),
    path('contact/', include('contact.urls')),
    path('api/v1.0/', include('index.api.urls', namespace='index_apis')),
    path('api/v1.0/', include('product.api.urls', namespace='product_apis')),
    path('__debug__/', include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

