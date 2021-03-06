from django.db import models

# Create your models here.
# from datetime import datetime, timedelta



class Customer(models.Model):	
	GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

	customer_id = models.CharField(default="C001", unique=True, blank=True, max_length=10)
	name = models.CharField(default="", blank=True, max_length=255)
	email = models.EmailField(unique=True, blank=False, null=False)
	contact_no = models.CharField(max_length=10, blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True, help_text="FloatField")
	longitude = models.FloatField(blank=True, null=True, help_text="FloatField")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name	



class Bookmark(models.Model):
	title = models.CharField(default="", blank=True, max_length=255)
	title_contains = models.CharField(default="", blank=True, max_length=255)
	url = models.URLField(max_length=200)
	source_name = models.CharField(default="", blank=True, max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title	


class CustomerBookmark(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="customer")
	bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, null=True, related_name="bookmark")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.customer)
	






































