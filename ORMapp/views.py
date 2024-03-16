from django.db.models import Q
from django.http import JsonResponse
from .models import BooksLanguage, BooksBook, BooksSubject, BooksBookshelf, BooksAuthor

def GutenbergDataListView(request):
    book_ids = [int(id) for id in request.GET.getlist('id', [])]
    languages = request.GET.getlist('language', None)
    mimetypes = request.GET.getlist('mimetype', None)
    subjects = request.GET.getlist('subjects', None)
    bookshelves = [int(shelf) for shelf in request.GET.getlist('bookshelf', [])]
    authors = request.GET.getlist('author', None)
    titles = request.GET.getlist('title', None)

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


    books_data = []
    for book in books_queryset:
        book_info = {
            'title': book.title,
            'author': book.authors.all().values_list('name', flat=True),
            'genre': book.media_type,
            'languages': book.bookslanguages.all().values_list('code', flat=True),
            'subjects': book.bookssubjects.all().values_list('name',flat= True),
            'bookshelves': book.booksshelves.all().values_list('id', flat=True),
            'download_links': book.booksformats.all().values_list('url', flat=True)
        }
        books_data.append(book_info)

    return JsonResponse({'total_books_count': len(books_data), 'books': books_data})
