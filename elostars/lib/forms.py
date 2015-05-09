from decimal import Decimal

from django import forms


class OneEightyDegreesField(forms.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_value", Decimal("180"))
        kwargs.setdefault("min_value", Decimal("-180"))
        kwargs.setdefault("max_digits", 15)
        kwargs.setdefault("decimal_places", 12)
        super(OneEightyDegreesField, self).__init__(*args, **kwargs)
