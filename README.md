## Flask Application Design to Display Recent News Articles

### HTML Files

- **index.html**:
   - This is the main page that will display the news articles.
   - It should include a header with a title like "Recent News Articles" and a list to display the article titles.

- **article.html**:
   - This is a template for displaying an individual news article.
   - It should include a title, author, date, and the article content.

### Routes

- **@app.route('/')**:
   - This route handles the root URL and displays the index page with the list of news article titles.
   - The view function for this route should query a data source (e.g., a database or API) and retrieve a list of recent news articles.
   - It should then pass this list to the index.html template for rendering.

- **@app.route('/article/<int:article_id>'**:
   - This route handles requests for individual news articles.
   - The view function for this route should receive the article ID as a parameter and query the data source to retrieve the corresponding article.
   - It should then pass the article details to the article.html template for rendering.