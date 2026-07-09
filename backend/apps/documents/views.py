from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Document
from .serializers import (
    DocumentUploadSerializer,
    DocumentSerializer,
)
from .services import DocumentService


class UploadDocumentView(CreateAPIView):
    serializer_class = DocumentUploadSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = DocumentService.upload(
            request.user,
            serializer.validated_data,
        )

        return Response(
            DocumentSerializer(document).data,
            status=status.HTTP_201_CREATED,
        )


class DocumentListView(ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DocumentService.list_documents(
            self.request.user
        )


class DocumentDetailView(RetrieveAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            Document,
            owner=self.request.user,
            id=self.kwargs["pk"],
        )


class DeleteDocumentView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            Document,
            owner=self.request.user,
            id=self.kwargs["pk"],
        )
class SummarizeDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        document = get_object_or_404(
            Document,
            id=pk,
            owner=request.user,
        )

        summary, cached = DocumentService.summarize(document)

        return Response(
            {
                "document_id": str(document.id),
                "title": document.title,
                "summary": summary,
                "cached": cached,
                "generated_at": document.summary_generated_at,
                "ai_model": document.ai_model,
            }
        )