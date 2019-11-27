from django.urls import path, include
from . import views

urlpatterns = [
	# path("api/register", views.register),
	path("api/paroles/<int:page>", views.paroles),
	path("api/paroles/<mot>/on/<date>/<int:page>", views.paroles_on),
	path("api/paroles/<mot>/before/<date>/<int:page>", views.paroles_before),
	path("api/paroles/<mot>/after/<date>/<int:page>", views.paroles_after),

	path("api/messages/<int:page>", views.messages),
	path("api/message/<slug>", views.message),
	path("api/messages/<mot>/on/<date>/<int:page>", views.messages_on),
	path("api/messages/<mot>/before/<date>/<int:page>", views.messages_before),
	path("api/messages/<mot>/after/<date>/<int:page>", views.messages_after),

	path("api/categories", views.categories),
	path("api/profile/<username>", views.profile),
]