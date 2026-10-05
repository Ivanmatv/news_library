from news_library.author import Author


class NewsPortal:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__authors: dict = {}
        self.__articles: dict = {}
        self.__TEXT_DICTIONARY_KEY = "text"
        self.__TITLE_DICTIONARY_KEY = "title"

    def get_name(self) -> str:
        return self.__name

    def add_author(self, author: Author) -> None:
        author_name = author.get_name()
        self.__authors[author_name] = self.__articles

    def remove_author(self, author: Author) -> None:
        author_name = author.get_name()
        self.__remove_key(author=author_name)

    def write_article(self, author: Author, text: str, title: str) -> None:
        author_name = author.get_name()
        article = self.__authors[author_name]

        if author_name in self.__authors:
            if title not in article:
                article = author.write_article(text=text, title=title)
                article_title = article.get_title()
                article_text = article.get_text()
                self.__articles[article_title] = article_text
            else:
                print("Такая статья уже есть!")
        else:
            print("Такого автора нет!")

    def remove_article(self, author: Author, title: str) -> None:
        author_name = author.get_name()
        self.__remove_key(author=author_name, dictionary_key=title)

    def publish_article(self, author: Author, title: str) -> None:
        author_name = author.get_name()
        empty_placeholder = ""
        article_title = self.__authors[author_name]

        if author_name in self.__authors and title in article_title:
            text = self.__authors[author_name].get(title, empty_placeholder)

            print(
                f"\tСтатья '{title}' опубликована "
                f"автором - {author_name}."
                f"{text}"
            )
        else:
            print("Такой статьи нет!")

    def __remove_key(self, author: str, dictionary_key=None):
        if author in self.__authors:
            if dictionary_key:
                del self.__authors[author][dictionary_key]
            else:
                del self.__authors[author]
        else:
            print("Такого автора нет!")
