from rest_framework import serializers

from .models import Document


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "title",
            "file",
        )

    def validate_file(self, file):
        if not file.name.lower().endswith(".pdf"):
            raise serializers.ValidationError(
                "Only PDF files are allowed."
            )

        max_size = 10 * 1024 * 1024  # 10 MB

        if file.size > max_size:
            raise serializers.ValidationError(
                "Maximum file size is 10MB."
            )

        return file


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "id",
            "title",
            "file",
            "file_size",
            "mime_type",
            "processing_status",
            "uploaded_at",
        )