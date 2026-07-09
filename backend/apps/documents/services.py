from .models import Document
from django.utils import timezone
from .pdf_service import PDFService
from .ai_service import AIService

#Performs CRUD operations on the Document model. This service is used by the views to interact with the database.
class DocumentService:

    @staticmethod
    def upload(owner, validated_data):
        uploaded_file = validated_data["file"]

        document = Document.objects.create(
            owner=owner,
            title=validated_data["title"],
            file=uploaded_file,
            file_size=uploaded_file.size,
            mime_type=uploaded_file.content_type,
        )

        return document

    @staticmethod
    def list_documents(user):
        return Document.objects.filter(owner=user)

    @staticmethod
    def get_document(user, document_id):
        return Document.objects.get(
            owner=user,
            id=document_id,
        )

    @staticmethod
    def delete_document(document):
        document.delete()
        
    @staticmethod
    def summarize(document):
        """
        Returns a tuple:
        (summary, cached)
        """

        # Return cached summary if available
        if document.summary:
            return document.summary, True

        # Extract PDF text
        text = PDFService.extract_text(document.file.path)

        # Limit text for MVP
        text = text[:12000]
         # Generate summary
        ai = AIService()
        summary = ai.summarize(text)

        # Save result
        document.summary = summary
        document.summary_generated_at = timezone.now()
        document.ai_model = "gemini-2.5-flash"
        document.processing_status = document.ProcessingStatus.COMPLETED

        document.save(
            update_fields=[
                "summary",
                "summary_generated_at",
                "ai_model",
                "processing_status",
            ]
        )
        return summary, False