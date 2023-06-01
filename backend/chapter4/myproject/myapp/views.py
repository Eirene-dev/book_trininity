from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book
from .serializers import BookSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    pagination_class = PageNumberPagination

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['publication_date', 'price']

    def get_queryset(self):
        queryset = super().get_queryset()

        # 요청에서 필터링 매개변수 가져오기
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)

        # 필터링 적용
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)

        # 정렬 적용
        ordering = self.request.query_params.get('ordering', None)
        if ordering in self.ordering_fields:
            queryset = queryset.order_by(ordering)

        return queryset


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# def create_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'myapp/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})