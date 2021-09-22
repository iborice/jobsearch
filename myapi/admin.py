from django.contrib import admin
from .models import Poste, Annonce, Categorie, Forme, Ville

admin.site.register(Annonce)
admin.site.register(Categorie)
admin.site.register(Forme)
admin.site.register(Poste)
admin.site.register(Ville)

# Register your models here.
