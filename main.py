from author import Author
from news_portal import NewsPortal


author = Author("Ваня")

title = "Python"
text = """
    Классы определяют шаблон, по которому создаются объекты. 
    Это основа ООП - правильное понимание классов и объектов 
    позволяет создавать гибкие и масштабируемые приложения.
    """
article = author.write_article(title=title, text=text)

news_portal_name = "Газета"
news_portal = NewsPortal(news_portal_name)

news_portal.add_author(author)
news_portal.add_title(article=article, author=author)
news_portal.add_text(article=article, author=author)
news_portal.publish_article(article)

news_portal.remove_text(author)
news_portal.publish_article(article)