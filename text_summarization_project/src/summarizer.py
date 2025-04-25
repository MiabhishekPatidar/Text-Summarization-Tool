import heapq
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, max_sentences=5):
    """Summarizes text to a controlled sentence limit."""
    if not text:
        return "No content available for summarization."

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Word frequency table
    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stop_words and word.isalnum():
            freq_table[word] = freq_table.get(word, 0) + 1

    # Sentence scoring
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                if len(sentence.split()) < 40:  # Avoid too long sentences
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_table[word]

    # Select top-ranked sentences with strict control
    best_sentences = heapq.nlargest(max_sentences, sentence_scores, key=sentence_scores.get)

    return ' '.join(best_sentences)
