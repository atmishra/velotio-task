import mock
from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase

from mytweepy.core.models import Account, Tweet
from mytweepy.core.serializers import AccountSerializer


def mocked_fetch_tweets_task(**kwargs):
    return 'I am Mocked'


class TestAccountAPI(APITestCase):
    """
    Test the /accounts endpoint
    """

    @staticmethod
    def create_accounts():
        screen_names = ['a', 'abc', 'ndtv', 'gade36']

        for screen_name in screen_names:
            Account.objects.create(screen_name=screen_name)

    def setUp(self):
        self.url = reverse('ListCreateAccounts')

    def test_get_request_returns_list_of_accounts(self):
        TestAccountAPI.create_accounts()
        response = self.client.get(self.url, {})
        eq_(response.status_code, 200)

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        eq_(response.data['results'], serializer.data)

    def test_get_request_returned_object_has_count(self):
        response = self.client.get(self.url, {})
        eq_(response.data['count'], 0)

        TestAccountAPI.create_accounts()
        response = self.client.get(self.url, {})
        eq_(response.data['count'], 4)

    @mock.patch('mytweepy.core.tasks.fetch_tweets_task', side_effect=mocked_fetch_tweets_task)
    def test_post_request_should_create_new_account(self, *args, **kwargs):
        data = {'screen_name': 'amitabh'}
        response = self.client.post(self.url, data)
        eq_(response.status_code, 201)
        eq_(Account.objects.count(), 1)


class TestTweetAPI(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(screen_name='random')
        self.url = reverse('ListTweets', kwargs=dict(account_id=self.account.id))
        print(self.url)

    def test_get_returns_list_of_tweets(self):
        # create tweets
        tweet_texts = ['random text', 'another random text', 'some funny tweet']
        for tweet in tweet_texts:
            Tweet.objects.create(text=tweet, account_id=self.account.id)

        response = self.client.get(self.url, {})
        eq_(response.status_code, 200)






