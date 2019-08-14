from django.urls import path
from blogging.views import list_view
from blogging.views import detail_view
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('post/', add_post, name="blog_posts"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feed/', LatestEntriesFeed()),
]
