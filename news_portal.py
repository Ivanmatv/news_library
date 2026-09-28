from news_library.article import Article
from news_library.author import Author


class NewsPortal:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__authors = {}
        self.__article = {}
        self.text_dictionary_key = "text"
        self.title_dictionary_key = "title"

    @property
    def name(self) -> str:
        return self.__name

    def _remove_logic(self, author_name: str, dictionary_key: str):
        if author_name in self.__authors:
            if dictionary_key:
                del self.__authors[author_name][dictionary_key]
            else:
                del self.__authors[author_name]
        else:
            print("Такого автора нет!")

    def add_author(self, author: Author) -> None:
        author_name = author.get_name()
        self.__authors[author_name] = self.__article

    def remove_author(self, author: Author) -> None:
        author_name = author.get_name()
        author_name_dictionary_key = "author_name"
        self._remove_logic(
            author_name=author_name,
            dictionary_key=author_name_dictionary_key
        )

    def add_title(self, article: Article, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            article_title = article.get_title()
            self.__article[self.title_dictionary_key] = article_title

    def remove_title(self, author: Author) -> None:
        author_name = author.get_name()
        title_dictionary_key = "title"
        self._remove_logic(
            author_name=author_name,
            dictionary_key=title_dictionary_key
        )

    def add_text(self, article: Article, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            article_text = article.get_text()
            self.__article[self.text_dictionary_key] = article_text

    def remove_text(self, author: Author) -> None:
        author_name = author.get_name()
        text_dictionary_key = "text"
        self._remove_logic(
            author_name=author_name,
            dictionary_key=text_dictionary_key
        )

    def publish_article(self, author: Author) -> None:
        author_name = author.get_name()
        if author_name in self.__authors:
            print(self.__authors)
            empty_placeholder = ""
            title = self.__authors[author_name].get(self.title_dictionary_key, empty_placeholder)
            text = self.__authors[author_name].get(self.text_dictionary_key, empty_placeholder)

            print(
                f"\tСтатья '{title}' опубликована "
                f"автором - {author_name}."
                f"{text}"
            )