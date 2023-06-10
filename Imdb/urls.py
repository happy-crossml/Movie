from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie import urls as movie_url
from movie.views import HomeView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('movies/', include(movie_url, namespace='movies')),
    path('', HomeView.as_view(), name='home'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
