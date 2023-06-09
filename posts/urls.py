from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    DraftPostListView,
    ArchivedPostListView,
)    
# can import entire 'views' from post vs. listing one by one 
# Just don't forget 'views.' in path


urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("drafts/", DraftPostListView.as_view(), name ="drafts"),
    path("archived/", ArchivedPostListView.as_view(), name = "archive"),    
    path("<int:pk>/", PostDetailView.as_view(), name="posts_details"),
    path("new/", PostCreateView.as_view(), name="posts_new"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="posts_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="posts_delete"),
]

# can also name url short like this:
# name="list"
# name="detail"
# name="new"