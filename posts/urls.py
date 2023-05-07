from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)    
# can import entire 'views' from post vs. listing one by one 
# Just don't forget 'views.' in path


urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name="posts_details"),
    path("new/", PostCreateView.as_view(), name="posts_new"),
]

# can also name url short like this:
# name="list"
# name="detail"
# name="new"