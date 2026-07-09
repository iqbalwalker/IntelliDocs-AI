#Extracts text from PDF files using the PyMuPDF library.

import fitz  # PyMuPDF


class PDFService:
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract all text from a PDF file.

        Args:
            file_path: Absolute path to the PDF

        Returns:
            A single string containing all extracted text.
        """
        document = fitz.open(file_path)

        text = []

        try:
            for page in document:
                page_text = page.get_text("text")

                if page_text:
                    text.append(page_text.strip())

            result = "\n".join(text).strip()
            if not result:
                raise ValueError("No readable text found in the PDF.")
            return result

        finally:
            document.close()