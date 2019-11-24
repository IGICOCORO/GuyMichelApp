from django.contrib import admin
from . models import *

class ParoleAdmin(admin.ModelAdmin):
    list_display = ("titre","photo","audio","date","categorie","slug",)
    list_filter = ("titre","date","categorie")
    ordering = ("titre","date","categorie")
    search_field = ("titre","date","categorie")
    prepopulated_fields = {'slug': ('titre', )}

class MessageAdmin(admin.ModelAdmin):
    list_display = ("titre","categorie" ,"photo","text","date","slug",)
    list_filter = ("titre","date","categorie")
    ordering = ("titre","date","categorie")
    search_field = ("titre","date","categorie")
    prepopulated_fields = {'slug': ('titre', )}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","bio","image","birth_date")
    list_filter = ("user","bio","image","birth_date")
    search_fields = ("user","bio","image","birth_date")

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    search_fields = ('name', )

admin.site.register(Parole, ParoleAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categorie, CategorieAdmin)

