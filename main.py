from author import Author
from article import Article
from news_portal import NewsPortal

author = Author("Ваня")

title = "Python"
text = """
    Классы определяют шаблон, по которому создаются объекты. 
    Это основа ООП - правильное понимание классов и объектов 
    позволяет создаватьгибкие и масштабируемые приложения.
    """

article = Article(title=title, text=text)
article_title = article.get_title()
article_text = article.get_text()

author_name = author.get_author_name()

news_portal_name = "Газета"

news_portal = NewsPortal(
    news_portal_name,
    article_title,
    author_name,
    article_text
)

news_portal.publish_article_title()
