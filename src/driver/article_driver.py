import json
import aiohttp
from src.interface.driver.article_driver import ArticleDriver


class ArticleDriverImpl(ArticleDriver):
    async def get_articles(self, page: int) -> dict:
        response = await aiohttp.request('GET', 'https://qiita.com/api/v2/items?page=1&per_page=20').coro
        articles = json.loads(await response.text())
        return {
            "articles": [{
                "id": a["id"],
                "body": a["body"]
            } for a in articles]
        }
