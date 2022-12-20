pip install google-cloud-language

import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/api/key.json"


text = "Elon Musk is a badass. He's sending rockets to mars while we're doing useless stuff."
document = language.types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

client = language.LanguageServiceClient()
sentiment = client.analyze_sentiment(document=document).document_sentiment

print(f"Sentiment score: {sentiment.score}")
print(f"Sentiment magnitude: {sentiment.magnitude}")