from django.urls import path
from . import views
from Helio.middleware import TokenMiddleware

urlpatterns = [
    path('home/', TokenMiddleware(views.dashboard), name='dashboard'),
]