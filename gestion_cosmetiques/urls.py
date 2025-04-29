from django.contrib import admin
from django.urls import path, include
from gestion_cosmetiques import settings
from produits import views  # Ajouter cette ligne
from django.urls import path, include
from django.conf.urls.static import static
from produits.views import login_view, logout_view
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('produits/', include('produits.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
