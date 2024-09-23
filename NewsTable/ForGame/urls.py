from django.urls import path

from .views import PostList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate, ConfirmUser

urlpatterns = [
    path('', PostList.as_view(), name='post'),
    path('<int:pk>', PostDetail.as_view(), name='postdetail'),
    path('search/', PostSearch.as_view(), name='postsearch'),
    path('create/', PostCreate.as_view(), name='postcreate'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='postdelete'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='postupdate'),
    path('confirm/', ConfirmUser.as_view(), name='confirm_user')
]
