import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def full_collection():
    collection = BooksCollector()
    collection.books_genre = {'Рождение Стальной крысы': 'Фантастика', 'Стальная Крыса поёт блюз': 'Фантастика',
                             'Стальная крыса на манеже': 'Фантастика', 'Новые приключения Стальной крысы': 'Фантастика', 'Оно': 'Ужасы',
                              'Лунный камень': 'Детективы'}
    return collection