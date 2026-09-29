class Article:
    def __init__(self, title: str, text: str, author: str):
        self.__title: str = title
        self.__text: str = text
        self.__author: str = author

    def get_title(self) -> str:
        return self.__title

    def get_text(self) -> str:
        return self.__text

    def get_author(self) -> str:
        return self.__author
