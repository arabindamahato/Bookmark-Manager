from django.contrib import admin
from bookmark_app.models import (
								Customer, 
								Bookmark, 
								CustomerBookmark, 
								)
admin.site.site_header = "Bookmark Manager"

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display = [
			'customer_id',
			'name',
			'email',
			'contact_no',
			'gender',
			'latitude',
			'longitude',
		]
	list_per_page = 5


	list_display_links = ['customer_id','name','email']

	list_editable = ['contact_no',]

	search_fields = ['customer_id','name', 'email', 'contact_no']

	list_filter = ['customer_id',]

	fields = [
		# while creating customer these field comes
		'customer_id',
		'name',
		'email',
		'contact_no',
		'gender',
		'latitude',
		'longitude',
	]


class BookmarkAdmin(admin.ModelAdmin):
	list_display = [
			'title',
			'title_contains',
			'url',
			'source_name',
			# 'bookmark_date',
		]

	list_per_page = 5


	list_display_links = ['title','url', 'title_contains']

	# list_editable = ['source_name',]

	search_fields = ['title', 'url', 'source_name']

	list_filter = ['title',]

	fields = [
		# while creating bookmark these field comes
		'title',
		'title_contains',
		'url',
		'source_name',
	]



class CustomerBookmarkAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"customer",
		"bookmark",
	]

	list_per_page = 5

	list_display_links = [
		"id",
		"customer",
		"bookmark",
	]

	search_fields = ['id', 'customer', 'bookmark']

	list_filter = ['customer',]

	fields = [
		# while creating customerBookmark  these field appear
		'customer',
		'bookmark',
		'is_active',
	]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(CustomerBookmark, CustomerBookmarkAdmin)