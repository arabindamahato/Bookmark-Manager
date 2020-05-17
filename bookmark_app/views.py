from django.shortcuts import render
from rest_framework import generics
from bookmark_app.models import Customer, Bookmark, CustomerBookmark
from bookmark_app.serializers import CustomerSerializer, BookmarkSerializer, CustomerBookmarkSerializer

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




class BookmarkList(generics.ListCreateAPIView):
	"""Browse all  Bookmark"""
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer

	ordering_fields = ['id',]

	search_fields = [
				'title', 
				'url',
				'source_name',
			]




class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
	"""Browse a particular Bookmark by using id"""
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer

	ordering_fields = ['id',]

	search_fields = [
				'title', 
				'url',
				'source_name',
			]



class CustomerBookmarkList(generics.ListAPIView):
	queryset = CustomerBookmark.objects.all()
	serializer_class = CustomerBookmarkSerializer

	ordering_fields = [
				'id',
			]

	search_fields = [
							
				'customer__id',
				'customer__latitude',
				'customer__longitude',
				'bookmark__source_name',
	]


class CustomerBookmarkCreate(generics.CreateAPIView):
	queryset = CustomerBookmark.objects.all()
	serializer_class = CustomerBookmarkSerializer

	