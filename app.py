from flask import Flask

from src.driver.article_driver import ArticleDriverImpl
from src.interactor.article_interactor import ArticleInteractor
from src.repository.article_repository import ArticleRepositoryImpl
from src.rest.article_resource import ArticleResource

app = Flask(__name__)

article_resource = ArticleResource(
    article_usecase=ArticleInteractor(
        article_repository=ArticleRepositoryImpl(
            article_driver=ArticleDriverImpl()
        )
    )
)

app.add_url_rule('/', view_func=article_resource.index)
