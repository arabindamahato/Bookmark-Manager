from django.urls import path
from bookmark_app import views

urlpatterns = [
	# customer related url
    path('customer/', views.CustomerList.as_view()),
    path('customer/<pk>/', views.CustomerDetail.as_view()),

    # bookmark related url
    path('bookmark/', views.BookmarkList.as_view()),
    path('bookmark/<pk>/', views.BookmarkDetail.as_view()),

    # customerBookmark url
    path('create/', views.CustomerBookmarkCreate.as_view()),
    path('browse/', views.CustomerBookmarkList.as_view()),


]
