from django.contrib import admin
from django.http import HttpRequest
from website.models import HelpPage
# Register your models here.

class WebsiteAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False
    pass

admin.site.register(HelpPage,WebsiteAdmin)