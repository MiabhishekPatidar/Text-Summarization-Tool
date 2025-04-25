import re
from nltk.tokenize import sent_tokenize

def clean_text(text):
    """Cleans text and ensures concise input for summarization."""
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    sentences = sent_tokenize(text)

    # Keep only a reasonable number of sentences for processing
    if len(sentences) > 15:
        sentences = sentences[:15]  # Limit input text to 15 sentences

    return ' '.join(sentences), sentences
