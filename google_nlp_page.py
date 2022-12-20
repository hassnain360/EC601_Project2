pip install google-cloud-language

import os
from google.cloud import language

import google.cloud
import google.cloud.language

# Replace with API key
api_key = "HIDDEN_MY_KEY_HAHAHAH"

# Initialize Google NLP client
client = google.cloud.language.LanguageServiceClient(credentials=api_key)

# Define URL to analyze
url = "https://www.cnn.com/2022/12/20/tech/elon-musk-twitter-polls/index.html"

# Analyze sentiment of text on page
document = google.cloud.language.types.Document(content=url, type=google.cloud.language.enums.Document.Type.WEB_PAGE)
sentiment = client.analyze_sentiment(document=document).document_sentiment

# Print results
print("Sentiment Score: {}".format(sentiment.score))
print("Sentiment Magnitude: {}".format(sentiment.magnitude))