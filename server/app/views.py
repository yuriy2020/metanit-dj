from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from app.models import Ticket
from app.serializers import TicketSerializer


# Create your views here.

# class TicketsList(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Ticket.objects.all()
#         serializer = TicketSerializer(queryset, many=True)
#         return Response(serializer.data)


class TicketsList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer