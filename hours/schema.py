import graphene

from graphene_django.types import DjangoObjectType

from .models import HourValue


class HourValueType(DjangoObjectType):
    class Meta:
        model = HourValue


class HoursQuery:
    hour_values = graphene.List(HourValueType)
    hour_value = graphene.Field(
        HourValueType,
        uuid=graphene.UUID()
    )

    def resolve_hour_values(self, info, **kwargs):
        return HourValue.objects.all()

    def resolve_hour_value(self, info, **kwargs):
        uuid = kwargs.get('uuid')

        if uuid is not None:
            return HourValue.objects.get(uuid=uuid)

        return None
