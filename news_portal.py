from news_library.article import Article
from news_library.author import Author


class NewsPortal:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__authors: list = []
        self.__article: dict = {}
        self.__TEXT_DICTIONARY_KEY = "text"
        self.__TITLE_DICTIONARY_KEY = "title"

    def get_name(self) -> str:
        return self.__name

    def add_author(self, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            self.__authors.append(author_name)
        else:
            print("Такой автор уже есть в списке!")

    def remove_author(self, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            self.__authors.remove(author_name)
        else:
            print("Такого автора нет в списке!")

    def add_title(self, article: Article, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            article_title = article.get_title()
            self.__article[self.__TITLE_DICTIONARY_KEY] = article_title

    def remove_title(self, author: Author) -> None:
        author_name = author.get_name()
        title_dictionary_key = "title"
        self.__remove_key(
            author_name=author_name,
            dictionary_key=title_dictionary_key
        )

    def add_text(self, article: Article, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            article_text = article.get_text()
            self.__article[self.__TEXT_DICTIONARY_KEY] = article_text

    def remove_text(self, author: Author) -> None:
        author_name = author.get_name()
        self.__remove_key(
            author_name=author_name,
            dictionary_key=self.__TEXT_DICTIONARY_KEY
        )

    def publish_article(self, article: Article) -> None:
        author_name = article.get_author()
        if author_name in self.__authors:
            empty_placeholder = ""
            title = self.__authors[author_name].get(self.__TITLE_DICTIONARY_KEY, empty_placeholder)
            text = self.__authors[author_name].get(self.__TEXT_DICTIONARY_KEY, empty_placeholder)

            print(
                f"\tСтатья '{title}' опубликована "
                f"автором - {author_name}."
                f"{text}"
            )

    def __remove_key(self, author_name: str, dictionary_key: str):
        if author_name in self.__authors:
            if dictionary_key:
                del self.__article[author_name][dictionary_key]
            else:
                del self.__article[author_name]
        else:
            print("Такого автора нет!")
