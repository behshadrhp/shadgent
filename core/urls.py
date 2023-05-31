from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('estate.api.urls')),
]

admin.site.site_header = 'ShadoGent Panel'
admin.site.index_title = 'ShadoGent admin site'
admin.site.site_title = 'Real Estate Consultant'
