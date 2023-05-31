from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})