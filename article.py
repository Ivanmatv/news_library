from news_library.author import Author


class Article:
    def __init__(self, title: str, text: str, author: Author):
        self.__title: str = title
        self.__text: str = text
        self.__author: object = author

    def get_title(self) -> str:
        return self.__title

    def get_text(self) -> str:
        return self.__text

    def get_author(self):
        author_name = self.__author.get_name()
        return author_name
