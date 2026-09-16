# “News Library”
Journalists upload articles to the news portal website. Each article has an author, but the author can write articles for third‑party platforms and is not part of the website.

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

## Installation

1) Clone repository
```
git clone https://github.com/Ivanmatv/news_library.git
```
2) Change directory
```
cd news_library
```

## Usage 

Launch the application
```
python main.py
```

## Result 

After lunch application, you receive message in the terminal
```
Статья Python опубликована автором Ваня
```

## Requirements
 - Python 