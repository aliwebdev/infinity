from django.db import models
from generic.models import GenericModel


class HourValue(GenericModel):
    value = models.DecimalField(
        default=25.,
        decimal_places=8,
        max_digits=20,
        blank=False,
    )

    date = models.CharField(
        unique=False,
        max_length=15,
        blank=False,
    )

    def __unicode__(self):
        return "%s, value: (%s, %s)" % (self.created_date, self.date, self.value)
