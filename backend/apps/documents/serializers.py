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
        allowed_extensions = (".pdf",".docx", ".txt")
        if not file.name.lower().endswith(allowed_extensions):
            raise serializers.ValidationError(
                "Only PDF, DOCX and TXT files are allowed."
            )

        max_size = 10 * 1024 * 1024  # 10 MB

        if file.size > max_size:
            raise serializers.ValidationError(
                "Maximum file size is 10MB."
            )

        return file
    
   #def validate_title(self, attrs):
    #    if not attrs.get("title"):
     #       attrs["title"] = attrs["file"].name
      #  return attrs 


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