from django.contrib import admin
from cw21.models import ContactInfo
from cw21.models import Person
from cw21.models import Group
# Register your models here.

admin.site.register(ContactInfo)
admin.site.register(Person)
admin.site.register(Group)
