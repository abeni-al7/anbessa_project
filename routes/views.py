from .models import Route
from .serializers import RouteSerializer
from rest_framework import viewsets
from rest_framework import permissions


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]
