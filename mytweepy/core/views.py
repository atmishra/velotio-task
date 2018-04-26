from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView

from mytweepy.core.models import Account, Tweet
from mytweepy.core.serializers import AccountSerializer, TweetSerializer


class AccountListCreateView(ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = ()
    queryset = Account.objects.all()


class TweetListView(ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = ()
    search_fields = ('text',)

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Tweet.objects.filter(account_id=account_id)
