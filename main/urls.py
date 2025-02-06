from django.urls import path
from .views import NewCollectionView, RecListView


urlpatterns = [
    path(
		route = 'collections/new/',
		view = NewCollectionView.as_view(),
		name = "new_collection"
    ),
    path(
		route = 'collections/<int:pk>/',
		view = RecListView.as_view(),
		name = "rec_list"
    ),
]