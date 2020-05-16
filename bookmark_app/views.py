from django.shortcuts import render
from rest_framework import generics
from bookmark_app.models import Customer, Bookmark
from bookmark_app.serializers import CustomerSerializer, BookmarkSerializer

# Create your views here.
 
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

	ordering_fields = ['id',]

	search_fields = [
				'name', 
				'email',
				'contact_no',
			]
 
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

	ordering_fields = ['id',]

	search_fields = [
				'name', 
				'email',
				'contact_no',
			]


class BookmarkCreate(generics.CreateAPIView):
	"""Create Bookmark"""
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer

	ordering_fields = ['id',]

	search_fields = [
				'title', 
				'url',
				'source_name',
			]


class BookmarkBrowse(generics.RetrieveAPIView):
	"""Browse a particular Bookmark by using id"""
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer

	ordering_fields = ['id',]

	search_fields = [
				'title', 
				'url',
				'source_name',
			]



class BookmarkList(generics.ListAPIView):
	"""Browse all  Bookmark"""
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer

	ordering_fields = ['id',]

	search_fields = [
				'title', 
				'url',
				'source_name',
			]