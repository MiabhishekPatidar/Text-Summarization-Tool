from src.web_scraper import fetch_article
from src.text_processing import clean_text
from src.summarizer import summarize_text

def main():
    """Fetch, process, and summarize a news article."""
    
    url = input("Enter a news article URL: ").strip()
    if not url:
        print("❌ Invalid input. Please enter a valid URL.")
        return

    article = fetch_article(url)
    if not article:
        print("❌ Failed to retrieve the article.")
        return
    
    cleaned_text, sentences = clean_text(article)
    summary = summarize_text(cleaned_text)

    print("\n📰 Original Article (First 5 Sentences):\n")
    print(' '.join(sentences[:5]) + " ...")  

    print("\n✨ Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
