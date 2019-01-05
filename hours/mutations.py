from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import HourValueForm


class HourValueMutation(DjangoModelFormMutation):
    class Meta:
        form_class = HourValueForm


class HoursMutation:
    create_hour_value = HourValueMutation.Field()
