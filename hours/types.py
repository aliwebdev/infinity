from graphene_django.types import DjangoObjectType
from .models import HourValue


class HourValueType(DjangoObjectType):
    class Meta:
        model = HourValue
