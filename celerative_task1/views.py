from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """

    queryset = Person.objects.all().order_by("-created_date")
    serializer_class = PersonSerializer
