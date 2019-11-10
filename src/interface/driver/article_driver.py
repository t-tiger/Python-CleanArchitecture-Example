from abc import ABCMeta, abstractmethod


class ArticleDriver(metaclass=ABCMeta):
    @abstractmethod
    async def get_articles(self, page: int) -> dict:
        raise NotImplementedError
