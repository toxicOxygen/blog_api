from rest_framework import generics,permissions
from .models import Post

from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class ListPost(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer