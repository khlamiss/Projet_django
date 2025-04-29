from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nom
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='produits/', null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.nom
