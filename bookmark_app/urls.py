from django.urls import path
from bookmark_app import views

urlpatterns = [
	# customer related url
    path('customer/', views.CustomerList.as_view()),
    path('customer/<pk>/', views.CustomerDetail.as_view()),

    # bookmark related url
    path('create/', views.BookmarkCreate.as_view()),
    path('browse/', views.BookmarkList.as_view()),
    path('browse/<pk>/', views.BookmarkBrowse.as_view()),

]
