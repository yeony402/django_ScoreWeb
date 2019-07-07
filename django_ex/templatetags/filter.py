from django import template
from django.contrib.auth.models import Group


register = template.Library()

@register.filter(name='has_group')
def has_group(user, manager):
    # group = Group.objects.get(name=manager)
    return True if user.groups.filter(name=manager).exists() else False

@register.filter(name='has_group_customuser')
def has_group_customuser(user, customuser):
    return True if user.groups.filter(name=customuser).exists() else False
