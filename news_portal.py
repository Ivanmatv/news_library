class NewsPortal:
    def __init__(
        self,
        name: str,
        article_title: str,
        article_author: str,
        article_text: str
    ) -> None:
        self.__name = name
        self.__article_title = article_title
        self.__article_author = article_author
        self.__article_text = article_text


    def publish_article_title(self) -> None:
        print(
            f"Статья {self.__article_title} опубликована "
            f"автором {self.__article_author}"
        )

    def publish_full_article(self) -> None:
        print(
            f"{self.__article_title} \n"
            f"{self.__article_text}"
        )