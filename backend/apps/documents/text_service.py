class TextService:
    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 4000,
    ):
        chunks = []

        start = 0

        while start < len(text):
            chunks.append(
                text[start:start + chunk_size]
            )

            start += chunk_size

        return chunks