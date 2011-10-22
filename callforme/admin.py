from django.contrib import admin

from models import (Contact, Call)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "phone", "birthday", "twitter", "frequency",)
    list_filter = ("user", )
admin.site.register(Contact, ContactAdmin)

class CallAdmin(admin.ModelAdmin):
    list_display = ("user", "contact", "time",)
    list_filter = ("user", )
admin.site.register(Call, CallAdmin)