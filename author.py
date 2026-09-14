from article import Article


class Author:
    def __init__(self, name: str):
        self.__name = name

    def get_author_name(self) -> str:
        return self.__name

    def write_article(self, title: str, text: str):
        article = Article(title, text)
        return article
