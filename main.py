
from flask import Flask, render_template, request
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database connection
conn = sqlite3.connect('news.db')
c = conn.cursor()

# Home page route
@app.route('/')
def index():
    # Fetch news articles from database
    c.execute('SELECT * FROM articles ORDER BY date DESC')
    articles = c.fetchall()
    return render_template('index.html', articles=articles)

# Individual article route
@app.route('/article/<int:article_id>')
def article(article_id):
    # Fetch specific article from database
    c.execute('SELECT * FROM articles WHERE id=?', (article_id,))
    article = c.fetchone()
    return render_template('article.html', article=article)

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
