#Performs AI services on documents, such as summarization, question answering, and more.
from django.conf import settings
from google import genai


class AIService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def summarize(self, text: str) -> str:
        prompt = f"""
You are an expert document analyst.

Summarize the following document.

The summary should:

- Be concise
- Preserve important information
- Use bullet points where appropriate
- Be easy to read

Document:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text