import uuid

from django.conf import settings
from django.db import models

from .utils import document_upload_path


class Document(models.Model):

    class ProcessingStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PROCESSING = "PROCESSING", "Processing"
        COMPLETED = "COMPLETED", "Completed"
        FAILED = "FAILED", "Failed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to=document_upload_path
    )

    file_size = models.PositiveBigIntegerField()

    mime_type = models.CharField(max_length=100)

    processing_status = models.CharField(
        max_length=20,
        choices=ProcessingStatus.choices,
        default=ProcessingStatus.PENDING,
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    summary = models.TextField(blank=True, default="")
    
    summary_generated_at = models.DateTimeField(
    null=True,
    blank=True
    )
    
    ai_model = models.CharField(
    max_length=50,
    blank=True,
    default=""
    )

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.title} ({self.owner.email})"