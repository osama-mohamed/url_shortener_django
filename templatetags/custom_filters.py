from django.template import Library

register = Library()

@register.filter
def format_timestamp(timestamp):
  return timestamp.strftime("%Y-%m-%d %I:%M:%Sp.m")