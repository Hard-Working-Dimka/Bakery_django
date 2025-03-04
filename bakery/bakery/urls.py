from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from cakes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API.urls')),

    path('shorten/', views.shorten_url, name='shorten_url'),

    re_path(r'^s/(?P<short_url>[a-zA-Z0-9]+)/$', views.redirect_to_long_url, name='redirect_to_long_url'),

    path('error/', views.error_page, name='error_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
