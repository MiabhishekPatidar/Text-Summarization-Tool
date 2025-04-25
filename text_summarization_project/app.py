from flask import Flask, request, render_template
from src.web_scraper import fetch_article_text
from src.text_processing import clean_text
from src.summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    url = ""
    error = ""

    if request.method == "POST":
        url = request.form.get("url")
        text = fetch_article_text(url)

        if not text or len(text) < 100:
            error = "Failed to extract enough content. Try another URL."
        else:
            cleaned_text, _ = clean_text(text)
            summary = summarize_text(cleaned_text)

    return render_template("index.html", summary=summary, url=url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
