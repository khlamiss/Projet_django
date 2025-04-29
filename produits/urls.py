from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('', views.accueil, name='accueil'),
    path('analytics/', views.accueil, name='analytics'), 
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('liste/', views.liste_produits, name='liste_produits'),
    path('modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)