from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializer import *


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class BooksAuthorListView(APIView):
    def get(self, request):
        queryset = BooksAuthor.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksAuthorSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count()  
        return response


class BooksBookListView(APIView):
    def get(self, request):
        queryset = BooksBook.objects.order_by('-download_count')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count()  
        return response


class BooksBookAuthorsListView(APIView):
    def get(self, request):
        queryset = BooksBookAuthors.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookAuthorsSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count()  
        return response


class BooksBookBookshelvesListView(APIView):
    def get(self, request):
        queryset = BooksBookBookshelves.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookBookshelvesSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count()  
        return response


class BooksBookLanguagesListView(APIView):
    def get(self, request):
        queryset = BooksBookLanguages.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookLanguagesSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count() 
        return response


class BooksBookSubjectsListView(APIView):
    def get(self, request):
        queryset = BooksBookSubjects.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookSubjectsSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count() 
        return response


class BooksBookshelfListView(APIView):
    def get(self, request):
        queryset = BooksBookshelf.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksBookshelfSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count() 
        return response


class BooksFormatListView(APIView):
    def get(self, request):
        queryset = BooksFormat.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksFormatSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count() 
        return response


class BooksLanguageListView(APIView):
    def get(self, request):
        queryset = BooksLanguage.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksLanguageSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count()  
        return response


class BooksSubjectListView(APIView):
    def get(self, request):
        queryset = BooksSubject.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BooksSubjectSerializer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.data['count'] = queryset.count() 
        return response
