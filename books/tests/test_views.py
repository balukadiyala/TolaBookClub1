import pytest

from books.models import Book, Review
from django.test import TestCase
from django.urls import reverse
from books.models import Book, Review

class BookDetailViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Test Author', summary='Test Summary')
        self.review = Review.objects.create(book=self.book, rating=5, comment='Excellent book')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.author)
        self.assertContains(response, self.book.summary)
        self.assertContains(response, self.review.comment)
        self.assertContains(response, 'Average Rating: 5')

class SubmitReviewViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Test Author', summary='Test Summary')

    def test_submit_review_view(self):
        response = self.client.post(reverse('submit_review', args=[self.book.id]), {
            'rating': 4,
            'comment': 'Good book'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

        self.assertEqual(Review.objects.first().rating, 4)



        self.assertEqual(Review.objects.first().comment, 'Good book')