import graphene

from .models import HourValue
from .types import HourValueType


class Query:
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
