from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts import views, urls
from projects import views, urls


from home import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)