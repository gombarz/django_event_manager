from django.contrib import admin
from .models import Event, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Display Category Model in Admin-Interface."""
    list_display = ("id", "name", "sub_title", "number_of_events")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Display Event Model in Admin-Interface."""
    list_display = ("id", "name", "author", "category", "is_active")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    actions = ["make_active", "make_inactive"]
    readonly_fields = ("name",)

    @admin.action(description="Set Event to active")
    def make_active(self, request, queryset):
        """Set all entries to active"""
        queryset.update(is_active=True)

    @admin.action(description="Set Event to inactive")
    def make_inactive(self, request, queryset):
        """Set all entries to inactive"""
        queryset.update(is_active=False)
