from rest_framework import serializers
from bookmark_app.models import Customer, Bookmark, CustomerBookmark

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = [
			'id',
			'customer_id',
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
			'title_contains',
			'url',
			'source_name',
		]

		read_only_fields = ["id", "is_active"]	



class CustomerBookmarkSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer()
	bookmark = BookmarkSerializer()
	class Meta:
		model = CustomerBookmark
		fields = [
			'id',
			'customer',
			'bookmark',
		]
		# fields = '__all__'

		# write_only_fields = ('customer', 'bookmark')