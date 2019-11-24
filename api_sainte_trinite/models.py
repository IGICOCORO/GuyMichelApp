from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Parole(models.Model):
    titre = models.CharField(unique=True, max_length=100)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    categorie = models.ForeignKey('Categorie', null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    audio = models.FileField(upload_to="audio/")
    date = models.DateField(verbose_name="Date de parution", default=timezone.now)
    slug = models.CharField(max_length=1000)

    def __str__(self):
    	return self.titre

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = str(self.categorie)+slugify(self.titre)
        super(Parole, self).save(*args, **kwargs)

class Message(models.Model):
    titre = models.CharField(unique=True, max_length=100)
    categorie = models.ForeignKey('Categorie', null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    text = models.TextField()
    date = models.DateField(verbose_name="Date de parution", default=timezone.now)
    slug = models.CharField(max_length=1000)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.text = self.text.replace('\r', '').replace('\n','<br>')
        if not self.slug: self.slug = str(self.categorie)+slugify(self.titre)
        super(Message, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="profile/")
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
    	return f"{self.user.first_name} {self.user.last_name}"

class Categorie(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="categorie/")
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
