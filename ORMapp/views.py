from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class BooksAuthorListView(APIView):
    def get(self, request):
        queryset = BooksAuthor.objects.all()
        serializer = BooksAuthorSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookListView(APIView):
    def get(self, request):
        queryset = BooksBook.objects.all()
        serializer = BooksBookSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookAuthorsListView(APIView):
    def get(self, request):
        queryset = BooksBookAuthors.objects.all()
        serializer = BooksBookAuthorsSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookBookshelvesListView(APIView):
    def get(self, request):
        queryset = BooksBookBookshelves.objects.all()
        serializer = BooksBookBookshelvesSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookLanguagesListView(APIView):
    def get(self, request):
        queryset = BooksBookLanguages.objects.all()
        serializer = BooksBookLanguagesSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookSubjectsListView(APIView):
    def get(self, request):
        queryset = BooksBookSubjects.objects.all()
        serializer = BooksBookSubjectsSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksBookshelfListView(APIView):
    def get(self, request):
        queryset = BooksBookshelf.objects.all()
        serializer = BooksBookshelfSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksFormatListView(APIView):
    def get(self, request):
        queryset = BooksFormat.objects.all()
        serializer = BooksFormatSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksLanguageListView(APIView):
    def get(self, request):
        queryset = BooksLanguage.objects.all()
        serializer = BooksLanguageSerializer(queryset, many=True)
        return Response(serializer.data)

class BooksSubjectListView(APIView):
    def get(self, request):
        queryset = BooksSubject.objects.all()
        serializer = BooksSubjectSerializer(queryset, many=True)
        return Response(serializer.data)
