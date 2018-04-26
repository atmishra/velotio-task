from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView

from mytweepy.core.models import Account, Tweet
from .tasks import fetch_tweets_task
from mytweepy.core.serializers import AccountSerializer, TweetSerializer


class AccountListCreateView(ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = ()
    queryset = Account.objects.all()

    def perform_create(self, serializer):
        account = serializer.save()

        # Call async Task to fetch Tweets
        fetch_tweets_task.delay(account.id)


class TweetListView(ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = ()
    search_fields = ('text',)

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Tweet.objects.filter(account_id=account_id)
