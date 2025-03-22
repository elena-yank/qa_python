import pytest
from main import BooksCollector
class TestBooksCollector:

    #проверка добавления книги и того, что добавилась именно одна
    def test_add_new_book_add_one_book_book_added(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        assert len(collector.books_genre) == 1

    #проверка того, что книга со слишком длинным названием не будет добавлена
    @pytest.mark.parametrize('name', ['This is a very long book name that should not be accepted'])
    def test_add_new_book_add_negative_input_book_not_added(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    #проверка установки жанра книги
    def test_set_book_genre_book_genre_set(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        collector.set_book_genre('Месть Стальной крысы', 'Фантастика')
        assert collector.books_genre['Месть Стальной крысы'] == 'Фантастика'

    #проверка получения жанра книги
    def test_get_book_genre_book__genre_got(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        collector.set_book_genre('Месть Стальной крысы', 'Фантастика')
        assert collector.books_genre.get('Месть Стальной крысы') == 'Фантастика'

    #проверка получения книг определённого жанра
    def test_get_books_with_specific_genre_books_got(self, full_collection):
        scifi_books = full_collection.get_books_with_specific_genre('Фантастика')
        expected_books = ['Рождение Стальной крысы', 'Стальная Крыса поёт блюз', 'Стальная крыса на манеже',
                          'Новые приключения Стальной крысы']
        assert scifi_books == expected_books

    #проверка получения словаря books_genre
    def test_get_books_genre_got(self, full_collection):
        books_genre = full_collection.books_genre
        assert full_collection.get_books_genre() == books_genre

    #проверка получения списка книг для детей
    def test_get_books_for_children_age_rating_filtered(self, full_collection):
        books_for_children = full_collection.get_books_for_children()
        assert list(filter(lambda x: full_collection.books_genre[x] == 'Ужасы' or full_collection.books_genre[x] == 'Детективы', books_for_children)) == []

    #проверка добавления книги в избранное
    def test_add_book_in_favorites_book_in_favorites(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        collector.add_book_in_favorites('Месть Стальной крысы')
        assert collector.favorites[0] == 'Месть Стальной крысы'

    #проверка удаления книги из избранного
    def test_delete_book_from_favorites__book_not_in_favorites(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        collector.add_book_in_favorites('Месть Стальной крысы')
        collector.delete_book_from_favorites('Месть Стальной крысы')
        assert 'Месть Стальной крысы' not in collector.favorites

    #проверка получения списка избранных книг
    def test_get_list_of_favorites_books_get_favorites_list(self, collector):
        collector.add_new_book('Месть Стальной крысы')
        collector.add_book_in_favorites('Месть Стальной крысы')
        assert collector.favorites == collector.get_list_of_favorites_books()