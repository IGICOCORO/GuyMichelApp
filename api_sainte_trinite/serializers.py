from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ParoleSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField("get_author")
	categorie = serializers.SerializerMethodField("get_categorie")
	photo = serializers.SerializerMethodField("get_photo")
	class Meta:
		model = Parole
		fields ='__all__'

	def get_author(self, parole):
		return parole.author.user.first_name+" "+parole.author.user.last_name

	def get_categorie(self, parole):
		return parole.categorie.name

	def get_photo(self, parole):
		return parole.categorie.image

class MessageSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField("get_author")
	categorie = serializers.SerializerMethodField("get_categorie")
	photo = serializers.SerializerMethodField("get_photo")
	class Meta:
		model = Message
		fields =('id', "titre","author","categorie","photo","date","slug")

	def get_author(self, parole):
		return parole.author.user.first_name+" "+parole.author.user.last_name

	def get_categorie(self, parole):
		return parole.categorie.name

	def get_photo(self, parole):
		return parole.categorie.image

class ProfileSerializer(serializers.ModelSerializer):
	firstname = serializers.SerializerMethodField("get_firstname")
	lastname = serializers.SerializerMethodField("get_lastname")
	class Meta:
		model = Profile
		fields =("firstname", "lastname", "bio", "image", "birth_date")

	def get_firstname(self, profile):
		return profile.user.first_name

	def get_lastname(self, profile):
		return profile.user.last_name

class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categorie
		fields = "__all__"
