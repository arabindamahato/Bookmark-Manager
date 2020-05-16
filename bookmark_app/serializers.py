from rest_framework import serializers
from bookmark_app.models import Customer, Bookmark

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
		fields = [
			'id',
			'title',
			'url',
			'source_name',
		]

		read_only_fields = ["id", "is_active"]