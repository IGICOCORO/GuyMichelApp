from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.core import exceptions

from .serializers import *
from .models import *

@api_view(["GET",])
def profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

@api_view(["GET",])
def paroles(request, page):
    paroles = Paginator(Parole.objects.all(), 5)

    if request.method=="GET":
        data = []
        if(page>=1 and page<=paroles.num_pages):
            serializer = ParoleSerializer(paroles.page(page), many=True)
            data = serializer.data
        else:  
            data = [{}]
        return Response(data)

@api_view(["GET",])
def paroles_by(request, categorie):
    try:
        categorie = Parole.objects.get(name=categorie)
        paroles = Parole.objects.filter(categorie=categorie)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ParoleSerializer(transaction, many=True)
        return Response(serializer.data)

@api_view(["GET",])
def paroles_on(request, mot, date, page):
    paroles = Parole.objects.filter(date=date)

    if mot!="*":
        paroles = paroles.filter(titre__contains=mot)

    paroles = Paginator(paroles, 5)

    if request.method=="GET":
        data = []
        if(page>=1 and page<=paroles.num_pages):
            serializer = ParoleSerializer(paroles.page(page), many=True)
            data = serializer.data
        else:  
            data = [{}]
        return Response(data)

@api_view(["GET",])
def paroles_before(request, mot, date, page):
    paroles = Parole.objects.filter(date__lt=date)
    if mot!="*":
        paroles = paroles.filter(titre__contains=mot)
    
    paroles = Paginator(paroles, 5)

    if request.method=="GET":
        data = []
        if(page>=1 and page<=paroles.num_pages):
            serializer = ParoleSerializer(paroles.page(page), many=True)
            data = serializer.data
        else:  
            data = [{}]
        return Response(data)

@api_view(["GET",])
def paroles_after(request, mot, date, page):
    paroles = Parole.objects.filter(date__gt=date)
    if mot!="*":
        paroles = paroles.filter(titre__contains=mot)

    paroles = Paginator(paroles, 5)

    if request.method=="GET":
        data = []
        if(page>=1 and page<=paroles.num_pages):
            serializer = ParoleSerializer(paroles.page(page), many=True)
            data = serializer.data
        else:  
            data = [{}]
        return Response(data)

@api_view(["GET",])
def message(request, slug):
    try:
        message = Message.objects.get(slug=slug).text
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        return Response({"message":message})

@api_view(["GET",])
def messages(request, page):
    messages = Paginator(Message.objects.all(), 5)

    if request.method=="GET":
        data = []
        if(page>=1 and page<=messages.num_pages):
            serializer = MessageSerializer(messages.page(page), many=True)
            data = serializer.data
        else:  
            data = []
        return Response(data)

@api_view(["GET",])
def messages_by(request, categorie):
    try:
        categorie = Message.objects.get(name=categorie)
        paroles = Message.objects.filter(categorie=categorie)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ParoleSerializer(transaction, many=True)
        return Response(serializer.data)

@api_view(["GET",])
def messages_on(request, date):
    messages = Message.objects.filter(date=date)

    if request.method=="GET":
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(["GET",])
def messages_before(request, date):
    messages = Message.objects.filter(date__lt=date)

    if request.method=="GET":
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(["GET",])
def messages_after(request, date):
    messages = Message.objects.filter(date__gt=date)

    if request.method=="GET":
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(["GET",])
def categories(request):
    categories = Categorie.objects.all()

    if request.method=="GET":
        serializer = InfoTransactionSerializer(categories, many=True)
        return Response(serializer.data)