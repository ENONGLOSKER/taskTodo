from django import template
from django.utils.timesince import timesince
import datetime

register = template.Library()

@register.filter
def custom_timesince_or_created(value):
    if isinstance(value, datetime.datetime):
        now = datetime.datetime.now(datetime.timezone.utc)
        diff = now - value
        if diff.total_seconds() < 60:
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return timesince(value) + " lalu"
    return value
