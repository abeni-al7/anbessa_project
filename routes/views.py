from .models import Route
from .serializers import RouteSerializer
from rest_framework import viewsets


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
