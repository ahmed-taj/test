import rest_framework.viewsets as viewsets

from .models import Account
from . import serializers


class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    serializer_class = serializers.AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'username'
