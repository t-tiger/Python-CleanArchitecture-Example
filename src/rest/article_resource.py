import asyncio

from flask import jsonify

from src.domain.article import Articles
from src.interface.usecase.article_usecase import ArticleUsecase


class ArticleResource:
    article_usecase: ArticleUsecase

    def __init__(self, article_usecase: ArticleUsecase):
        self.article_usecase = article_usecase

    def index(self):
        main_group: Articles = asyncio.run(self.article_usecase.get_list(0))
        return jsonify(articles_response(main_group))


def articles_response(articles: Articles) -> dict:
    return {
        "items": [{
            "id": article.id,
            "body": article.body
        } for article in articles.values]
    }
