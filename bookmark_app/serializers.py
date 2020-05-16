from rest_framework import serializers
from bookmark_app.models import Customer, Bookmark, CustomerBookmark

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = [
			'id',
			'name',
			'email',
			'contact_no',
			'gender',
			'latitude',
			'longitude',
		]

		read_only_fields = ["id", "is_active"]

class BookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bookmark
		# fields = '__all__'
		fields = [
			'id',
			'title',
			'url',
			'source_name',
		]

		read_only_fields = ["id", "is_active"]	



class CustomerBookmarkSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer(read_only=True, many=True)
	bookmark = BookmarkSerializer(read_only=True, many=True)
	class Meta:
		model = CustomerBookmark
		fields = [
			'id',
			'customer',
			'bookmark',
		]
		# fields = '__all__'

		# write_only_fields = ('customer', 'bookmark')