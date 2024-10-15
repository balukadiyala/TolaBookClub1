import pytest
from django.test import TestCase
import pytest
from django.test import TestCase
from books.forms import ReviewForm
from django.test import TestCase
from books.forms import ReviewForm

class ReviewFormTest(TestCase):
    def test_review_form_valid(self):
        form_data = {'rating': 5, 'comment': 'Excellent book'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid(self):
        form_data = {'rating': 6, 'comment': 'Invalid rating'}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())