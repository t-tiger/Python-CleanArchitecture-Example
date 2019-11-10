from abc import ABCMeta, abstractmethod

from src.domain.article import Articles


class ArticleUsecase(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self, page: int) -> Articles:
        raise NotImplementedError
