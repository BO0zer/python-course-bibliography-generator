"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class DissertationModel(BaseModel):

    """
    Модель диссертации:
    .. code-block::
        DissertationModel(
            authors="Иванов И.М., Петров С.Н.",
            dissertation_title="Наука как искусство",
            canddoc="канд.",
            science="экон."
            code="01.01.01"
            city="СПб.",
            year=2020,
            pages=999,
        )
    """

    authors: str
    dissertation_title: str
    canddoc: str
    science: str
    code: str
    city: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class MagazineArticleModel(BaseModel):
    """
    Модель статьи из журнала:
    .. code-block::
        MagazineArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            magazine_title="Научный журнал",
            year=2020,
            magazine_number=1,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    magazine_title: str
    year: int = Field(..., gt=0)
    magazine_number: int = Field(..., gt=0)
    pages: str
