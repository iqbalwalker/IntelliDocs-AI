from django.urls import path
from .views import (
    UploadDocumentView,
    DocumentListView,
    DocumentDetailView,
    DeleteDocumentView,
    SummarizeDocumentView
)

urlpatterns = [
    path(
        "upload/",
        UploadDocumentView.as_view(),
        name="upload-document",
    ),

    path(
        "",
        DocumentListView.as_view(),
        name="list-documents",
    ),

    path(
        "<uuid:pk>/",
        DocumentDetailView.as_view(),
        name="document-detail",
    ),

    path(
        "<uuid:pk>/delete/",
        DeleteDocumentView.as_view(),
        name="delete-document",
    ),
    
    path(
    "<uuid:pk>/summarize/",
    SummarizeDocumentView.as_view(),
    name="summarize-document",
),
]