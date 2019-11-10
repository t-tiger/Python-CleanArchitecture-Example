from src.domain.article import Articles
from src.interface.repository.article_repository import ArticleRepository
from src.interface.usecase.article_usecase import ArticleUsecase


class ArticleInteractor(ArticleUsecase):
    article_repository: ArticleRepository

    def __init__(self, article_repository: ArticleRepository):
        self.article_repository = article_repository

    async def get_list(self, page: int) -> Articles:
        return await self.article_repository.get_list(page)
