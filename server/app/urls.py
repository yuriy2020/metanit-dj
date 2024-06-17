from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from app.views import TicketsList
#
# router = DefaultRouter()
# router.register(r'tickets', TicketsList)
urlpatterns = [
    path('tickets', TicketsList.as_view()),
]
