from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "processing_status",
        "uploaded_at",
    )

    search_fields = (
        "title",
        "owner__email",
    )

    list_filter = (
        "processing_status",
    )