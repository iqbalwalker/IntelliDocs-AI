import uuid
from pathlib import Path

def document_upload_path(instance, filname):
    extension = Path(filname).suffix
    return(
        f"documents/{instance.owner.id}/{uuid.uuid4()}{extension}"
    )