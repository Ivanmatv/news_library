from article import Article


class Author:
    def __init__(self, name: str):
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name

    def write_article(self, text: str, title: str) -> Article:
        article = Article(text=text, title=title, author=self.__name)
        return article
