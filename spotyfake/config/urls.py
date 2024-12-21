from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested.routers import NestedDefaultRouter #Cria rotas aninhadas com base em uma relação. Ex: /artistas/{artista_pk}/albuns/


from api import views

router = routers.DefaultRouter() # define as rotas principais, como /artistas/.
router.register(r'artistas', views.ArtistaViewSet, basename='artistas')
router.register(r'albuns', views.AlbumViewSet, basename='albuns')
router.register(r'musicas', views.MusicaViewSet, basename='musicas')


# Rotas aninhadas para Álbuns (relacionados a Artistas)
artista_router = NestedDefaultRouter(router, r'artistas', lookup='artista') # lookup define a chave usada para associar os modelos na URL
artista_router.register(r'albuns', views.AlbumViewSet, basename='artista-albuns')

# Rotas aninhadas para Músicas (relacionadas a Álbuns)
album_router = NestedDefaultRouter(artista_router, r'albuns', lookup='album')
album_router.register(r'musicas', views.MusicaViewSet, basename='album-musicas')

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),           # rotas principal
    path('', include(artista_router.urls)),   # rotas aninhadas de Álbuns
    path('', include(album_router.urls)),     # rotas aninhadas de músicas
]

# urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


