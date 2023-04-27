from django.utils import timezone
from django.core.exceptions import ValidationError

def datetime_in_past(value) -> None:
    """Raise Validation Error if datetime is in past."""
    if value <= timezone.now():
        raise ValidationError(
            "The date of the event should not be in the past"
        )
