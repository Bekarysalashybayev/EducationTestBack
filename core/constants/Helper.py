from enum import Enum
from django.utils.translation import gettext_lazy as _


class Choice(Enum):
    @classmethod
    def choices(cls):
        return [(c.value, _(c.name)) for c in cls]

    @classmethod
    def list(cls):
        return [c.value for c in cls]

    def __str__(self):
        return self.value
