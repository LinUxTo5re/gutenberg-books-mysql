from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import BooksLanguage, BooksBook, BooksSubject, BooksBookshelf, BooksAuthor
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi


@api_view(['GET'])
def GutenbergDataListView(request):
    if len(request.GET.getlist('id')) == 1:
        try:
            book_ids = [int(num) for num_str in request.GET.getlist('id') for num in num_str.split(',')]
        except:
            book_ids = [int(id) for id in request.GET.getlist('id', [])]
    else:
        book_ids = [int(id) for id in request.GET.getlist('id', [])]

    if len(request.GET.getlist('language')) == 1:
        try:
            languages = [lang.strip() for item in request.GET.getlist('language') for lang in item.split(',')]
        except:
            languages = request.GET.getlist('language', None)
    else:
        languages = request.GET.getlist('language', None)
    
    if len(request.GET.getlist('mimetype')) == 1:
        try:
            mimetypes = [mt.strip() for item in request.GET.getlist('mimetype') for mt in item.split(',')]
        except:
            mimetypes = request.GET.getlist('mimetype', None)
    else:
        mimetypes = request.GET.getlist('mimetype', None)

    if len(request.GET.getlist('subjects')) == 1:
        try:
            subjects = [sub.strip() for item in request.GET.getlist('subjects') for sub in item.split(',')]
        except:
            subjects = request.GET.getlist('subjects', None)
    else:
        subjects = request.GET.getlist('subjects', None)

    if len(request.GET.getlist('bookshelf')) == 1:
        try:
            bookshelves = [int(bs) for item in request.GET.getlist('bookshelf') for bs in item.split(',')]
        except:
            bookshelves = [int(shelf) for shelf in request.GET.getlist('bookshelf', [])]
    else:
        bookshelves = [int(shelf) for shelf in request.GET.getlist('bookshelf', [])]

    if len(request.GET.getlist('author')) == 1:
        try:
            authors = [auth.strip() for item in request.GET.getlist('author') for auth in item.split(',')]
        except:
            authors = request.GET.getlist('author', None)
    else:
        authors = request.GET.getlist('author', None)

    if len(request.GET.getlist('title')) == 1:
        try:
            titles = [ti.strip() for item in request.GET.getlist('title') for ti in item.split(',')]
        except:
            titles = request.GET.getlist('title', None)
    else:
        titles = request.GET.getlist('title', None)

    page_number = int(request.GET.get('page', 1))

    books_queryset = BooksBook.objects.all()

    if book_ids:
        books_queryset = books_queryset.filter(gutenberg_id__in=book_ids)
    if languages:
        language_ids = list(BooksLanguage.objects.filter(code__in=languages).values_list('id', flat=True))
        if language_ids:
            books_queryset = books_queryset.filter(booksbooklanguages__language_id__in=language_ids)
    if mimetypes:
        books_queryset = books_queryset.filter(booksformat__mime_type__in=mimetypes)
    if subjects:
        subject_ids = []
        for subject in subjects:
            subject_ids.extend(BooksSubject.objects.filter(name__icontains=subject).values_list('id', flat=True))
        if subject_ids:
            books_queryset = books_queryset.filter(booksbooksubjects__subject_id__in=subject_ids)
    if bookshelves:
        books_queryset = books_queryset.filter(booksbookbookshelves__bookshelf_id__in=bookshelves)
    if authors:
        author_ids = []
        for author in authors:
            author_ids.extend(BooksAuthor.objects.filter(name__icontains=author).values_list('id', flat=True))
        if author_ids:
            books_queryset = books_queryset.filter(booksbookauthors__author_id__in=author_ids)
    if titles:
        title_query = Q()
        for title in titles:
            title_query |= Q(title__icontains=title)
        books_queryset = books_queryset.filter(title_query)

    books_queryset = books_queryset.order_by('-download_count')

    paginator = Paginator(books_queryset, 20)
    try:
        books_page = paginator.page(page_number)
    except:
        books_page = []

    books_data = []
    for book in books_page:
        book_info = {
            'title': book.title,
            'author': list(book.authors.all().values_list('name', flat=True)),
            'genre': book.media_type,
            'languages': list(book.bookslanguages.all().values_list('code', flat=True)),
            'subjects': list(book.bookssubjects.all().values_list('name', flat=True)),
            'bookshelves': list(book.booksshelves.all().values_list('id', flat=True)),
        }
        books_data.append(book_info)

    has_next_page = books_page.has_next()

    next_page_url = None
    if has_next_page:
        next_page_number = page_number + 1
        next_page_url = f"?page={next_page_number}"

    response_data = {
        'total_books_count': paginator.count,
        'books_per_page': 20,
        'current_page': books_page.number,
        'total_pages': paginator.num_pages,
        'has_next_page': has_next_page,
        'next_page_url': next_page_url,
        'books': books_data
    }

    return JsonResponse(response_data)

GutenbergDataListView = swagger_auto_schema(
    method='GET',
    responses={200: 'OK'},
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="gutenberg ID", type=openapi.TYPE_STRING,required=False, explode=True),
        openapi.Parameter('language', openapi.IN_QUERY, description="langues code (eg: en, fr)", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('mimetype', openapi.IN_QUERY, description="mime type (eg: text/plain)", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('subjects', openapi.IN_QUERY, description="subjects", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('bookshelf', openapi.IN_QUERY, description="bookshelf ID", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('author', openapi.IN_QUERY, description="author name", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('title', openapi.IN_QUERY, description="book title", type=openapi.TYPE_STRING, required=False, explode=True),
        openapi.Parameter('page', openapi.IN_QUERY, description="pagination", type=openapi.TYPE_STRING, required=False, explode=True),
   
    ]
)(GutenbergDataListView)