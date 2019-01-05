import uuid
from django.db import models


class GenericModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def is_created(self):
        """
        Returns the current state of model objects (adding state or not)
        We cannot use self.pk is None cause pk has been overloaded by uuid logic
        So, we use _state.adding
        Returns:
            bool: adding state or not
        """
        return self._state.adding

    @property
    def highlights(self):
        return getattr(self, '_highlights', {})

    class Meta:
        abstract = True
