from src.domain.article import Article, Articles
from src.interface.driver.article_driver import ArticleDriver
from src.interface.repository.article_repository import ArticleRepository


class ArticleRepositoryImpl(ArticleRepository):
    article_driver: ArticleDriver

    def __init__(self, article_driver: ArticleDriver):
        self.article_driver = article_driver

    async def get_list(self, page: int) -> Articles:
        res = await self.article_driver.get_articles(page)
        return Articles(
            values=[
                Article(id=a["id"], body=a["body"])
                for a in res["articles"]
            ]
        )
