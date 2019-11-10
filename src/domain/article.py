from dataclasses import dataclass

from src.domain.collection import Collection


@dataclass(frozen=True)
class Article:
    id: str
    body: str


@dataclass(frozen=True)
class Articles(Collection[Article]):
    values: [Article]
