from author import Author
from news_portal import NewsPortal


author = Author("Ваня")

news_portal_name = "Газета"
news_portal = NewsPortal(news_portal_name)
news_portal.add_author(author)

title_python = "Python"
text_python = """
    Классы определяют шаблон, по которому создаются объекты. 
    Это основа ООП - правильное понимание классов и объектов 
    позволяет создавать гибкие и масштабируемые приложения.
    """
news_portal.write_article(author=author, title=title_python , text=text_python)
news_portal.publish_article(author=author, title=title_python)
print()

title_java = "Java"
text_java = """
    Популярный объектно-ориентированный язык программирования 
    общего назначения и программная платформа, созданные компанией 
    Sun Microsystems (входит в Oracle).
    """

news_portal.write_article(author=author, title=title_java , text=text_java)
news_portal.publish_article(author=author, title=title_java)
