from unittest import TestCase

from asyncmock import AsyncMock

from src.domain.article import Article, Articles
from src.interface.driver.article_driver import ArticleDriver
from src.repository.article_repository import ArticleRepositoryImpl
from tests import async_test


class DriverMock(ArticleDriver):
    async def get_articles(self, page: int) -> dict:
        raise NotImplementedError


class TestArticleRepository(TestCase):
    @async_test
    async def test_get(self):
        get_main_group_mock = AsyncMock(return_value={"articles": [
            {"id": "1", "body": "test"}
        ]})

        driver = DriverMock()
        driver.get_articles = get_main_group_mock
        repository = ArticleRepositoryImpl(article_driver=driver)

        self.assertEqual(
            await repository.get_list(1),
            Articles(values=[Article(id="1", body="test")])
        )
        get_main_group_mock.assert_called_with(1)
