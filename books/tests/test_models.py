from django.test import TestCase
from books.models import Book, Review

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Test Author', summary='Test Summary')

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.summary, 'Test Summary')

    def test_average_rating_no_reviews(self):
        self.assertEqual(self.book.average_rating(), 0)

    def test_average_rating_with_reviews(self):
        Review.objects.create(book=self.book, rating=4, comment='Good book')
        Review.objects.create(book=self.book, rating=2, comment='Not so good')
        self.assertEqual(self.book.average_rating(), 3)

class ReviewModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Test Author', summary='Test Summary')
        self.review = Review.objects.create(book=self.book, rating=5, comment='Excellent book')

    def test_review_creation(self):
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Excellent book')