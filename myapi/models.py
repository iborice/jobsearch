from django.db import models
import django.utils.timezone
from django.core.exceptions import ValidationError

#cest le modele plutot des entreprises ici
class Annonce(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    icone = models.ImageField(upload_to='myapi/icones/',default='myapi/default.jpg')   
    def __str__(self):
        return self.name
    
    def clean(self):
        if self.icone.width != 100 or self.icone.height != 100:
            raise ValidationError('les dimensions de l\'image doivent etre de 100*100')

#modele des annonces
class Poste(models.Model):
    annonce = models.ForeignKey('Annonce',on_delete=models.CASCADE)
    categories = models.ManyToManyField('Categorie',related_name='domaines')
    date = models.DateField(default=django.utils.timezone.now)
    date_expiration = models.DateField()
    date_publication = models.DateField()
    description = models.TextField()
    forme = models.ForeignKey('Forme',on_delete=models.CASCADE)
    intitule = models.CharField(max_length=60)
    nombre = models.PositiveIntegerField(default=1)
    experience_min = models.PositiveIntegerField(default=0)
    villes = models.ManyToManyField('Ville',related_name='lieux')

    def __str__(self):
        return self.intitule

#indique s'il s'agit d'un stage ou d'un cdd etc...
class Forme(models.Model):
    intitule = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.intitule

class Categorie(models.Model):
    intitule = models.CharField(max_length=60)
    
    def __str__(self):
        return self.intitule
# Create your models here.

class Ville(models.Model):
    intitule = models.CharField(max_length=60)

    def __str__(self):
        return self.intitule