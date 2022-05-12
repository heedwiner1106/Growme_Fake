from django.urls import path
from . import views

app_name = 'Site'
urlpatterns = [
	path('list/', views.SiteListView.as_view(), name='list_sites'),
	path('create/', views.SiteCreateView.as_view(), name='site_create'),
]
