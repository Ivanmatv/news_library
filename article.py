class Article:
    def __init__(self, title: str, text: str):
        self.__title: str = title
        self.__text: str = text

    def get_title(self) -> str:
        return self.__title

    def get_text(self):
        return self.__text
