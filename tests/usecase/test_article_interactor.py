from unittest import TestCase

from asyncmock import AsyncMock

from src.domain.article import Article, Articles
from src.interactor.article_interactor import ArticleInteractor
from src.interface.repository.article_repository import ArticleRepository
from tests import async_test


class RepositoryMock(ArticleRepository):
    async def get_list(self, page: str) -> Articles:
        raise NotImplementedError


class TestArticleInteractor(TestCase):
    @async_test
    async def test_get(self):
        get_mock = AsyncMock(return_value=Article(id="1", body='test'))

        repo = RepositoryMock()
        repo.get_list = get_mock
        usecase = ArticleInteractor(article_repository=repo)

        self.assertEqual(await usecase.get_list(1), Article(id="1", body="test"))
        get_mock.assert_called_with(1)
