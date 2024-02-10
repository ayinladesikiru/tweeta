from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .pagination import DefaultPaginationClass

from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer


# Create your views here.


class TweetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPaginationClass
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentViewSet(ListCreateAPIView, RetrieveDestroyAPIView, GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.select_related('tweet').filter(tweet_id=self.kwargs['tweet_pk'])
