from google.cloud import language_v2


def analyze_sentiment(text_content: str = "I am so happy and joyful.") -> None:
    """
    Analyzes Sentiment in a string.

    Args:
      text_content: The text content to analyze.
    """

    client = language_v2.LanguageServiceClient()

    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

    language_code = "en"
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    encoding_type = language_v2.EncodingType.UTF8

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )
    # Get overall sentiment of the input document
    #print(f"score: {response.document_sentiment.score}, magnitude: {response.document_sentiment.magnitude}")
    print(f"score: {response.document_sentiment.score}, magnitude: {response.document_sentiment.magnitude}")

