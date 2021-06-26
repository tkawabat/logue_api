from django.contrib import admin
from .models import User, Scenario
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Scenario)
admin.site.register(User, MarkdownxModelAdmin)