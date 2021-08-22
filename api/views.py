from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Post, Task


class CreateUserView(generics.CreateAPIView):
    """
    ユーザーの新規作成エンドポイント
    """

    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class PostListView(generics.ListAPIView):
    """
    投稿一覧を取得するエンドポイント
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class PostRetrieveView(generics.RetrieveAPIView):
    """
    idに基づいて特定のブログデータを取得するエンドポイント
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class TaskListView(generics.ListAPIView):
    """
    タスク一覧を取得するエンドポイント
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny, )


class TaskRetrieveView(generics.RetrieveAPIView):
    """
    idに基づいて特定のタスクデータを取得するエンドポイント
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny, )


class TaskViewSet(viewsets.ModelViewSet):
    """
    タスクデータの新規作成、取得、更新、削除(CRUD)のエンドポイント
    パーミッションはデフォルト(JWTトークン認証)を使用
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
