# “News Library”
Journalists upload articles to the news portal website. Each article has an author, but the author can write articles for third‑party platforms and is not part of the website.

 - Conditions: Create a structure that allows the author to write an article and publish it. After publication, the console should display: “Article [title] published by author [name].”

## Structure

### author.py
 - class Author:

    It responsible for storing the author’s name and writing the article.

    fields:
    - name - Name of the author article 
    
    methods:
   - get_author_name - Return author name
   - write_article - Create and return the article

### article.py

 - class Article.py
    
    It returns article title and article text

    fields:
   - title - The title of the article
   - text - The text of the article
   
    methods:
   - get_title - Return the title of the article
   - get_text - Return the text of the article
 
### news_portal.py

 - class NewsPortal
    
    It publishes the article
    
    fields:
   - name - Name of the news portal
   - article_title - The title of the article
   - article_author - Name of the author an article
   - article_text - The text of the article
   
    methods:
   - publish_article_title - Publish only article title and article name
   - publish_full_article - Publish only article title and article text