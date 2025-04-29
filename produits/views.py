from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit , Categorie
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            # Vérifier si l'utilisateur existe dans la base de données
            if User.objects.filter(username=username).exists():
                messages.error(request, "Mot de passe incorrect")
            else:
                messages.error(request, "Identifiants invalides")
            return render(request, 'login.html', {'username': username})
    
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def accueil(request):
    context = {
        'total_produits': Produit.objects.count(),
        'stock_faible': Produit.objects.filter(quantite__lt=10).count(),
        'total_categories': Categorie.objects.count(),
        'derniers_produits': Produit.objects.order_by('-date_creation')[:5],
        'categories_noms': list(Categorie.objects.values_list('nom', flat=True)),
        'categories_counts': list(Categorie.objects.annotate(count=Count('produit')).values_list('count', flat=True))
    }
    return render(request, 'produits/acceuil.html', context)
@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})
@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        quantite = request.POST['quantite']
        image = request.FILES.get('image')  # Récupère l'image envoyée
        Produit.objects.create(nom=nom, description=description, prix=prix, quantite=quantite, image=image)
        return redirect('liste_produits')

    return render(request, 'produits/ajouter.html')
@login_required
def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.nom = request.POST['nom']
        produit.description = request.POST['description']
        produit.prix = request.POST['prix']
        produit.quantite = request.POST['quantite']
        produit.save()
        return redirect('liste_produits')
    return render(request, 'produits/modifier.html', {'produit': produit})
# produits/views.py
@login_required
def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/supprimer.html', {'produit': produit})