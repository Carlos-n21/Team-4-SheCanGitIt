from django.utils.html import format_html
from django.contrib import admin
from .models import WomenInTech

@admin.register(WomenInTech)
class WomenInTechAdmin(admin.ModelAdmin):
    list_display = ("name", "preview_image")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius:4px;" />', obj.image.url)
        return "-"
    preview_image.short_description = "Image"