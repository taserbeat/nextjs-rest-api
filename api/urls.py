from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, TaskViewSet, TaskListView, TaskRetrieveView, PostListView, PostRetrieveView

router = routers.DefaultRouter()

router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # 投稿一覧
    path('list-post/', PostListView.as_view(), name='list-post'),

    # 投稿の詳細
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),

    # タスク一覧
    path('list-task/', TaskListView.as_view(), name='list-task'),

    # タスクの詳細
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),

    # 新規ユーザー登録
    path('register/', CreateUserView.as_view(), name='register'),

    # JWT認証
    path('auth/', include('djoser.urls.jwt')),

    # ルーター情報
    path('', include(router.urls)),
]
