from django.core.management.base import BaseCommand

from mytweepy.core.utils import fetch_tweets_for_account
from mytweepy.core.models import Account, Tweet


class Command(BaseCommand):
    help = 'Fetch tweets for added accounts'

    def handle(self, *args, **options):
        for account in Account.objects.all():
            tweets = fetch_tweets_for_account(account.screen_name)
            for tweet in tweets:
                Tweet.objects.create(account_id=account.id,
                                     text=tweet.text)
        self.stdout.write(self.style.SUCCESS('Successfully Fetched Tweets'))
