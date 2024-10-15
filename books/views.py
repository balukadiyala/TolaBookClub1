from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from .forms import ReviewForm


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    average_rating = book.average_rating()
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews, 'average_rating': average_rating})


def submit_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'books/submit_review.html', {'form': form})