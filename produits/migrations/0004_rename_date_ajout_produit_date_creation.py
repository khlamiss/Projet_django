# Generated by Django 5.2 on 2025-04-27 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_produit_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='date_ajout',
            new_name='date_creation',
        ),
    ]
