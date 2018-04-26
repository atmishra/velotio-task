from celery.task import task
from celery.utils.log import get_task_logger

from mytweepy.core import utils
from mytweepy.core.models import Account, Tweet

logger = get_task_logger(__name__)


@task(name="Fetch Tweets for account")
def fetch_tweets_task(account_id):
    """
    Fetch Tweets for account with account_id
    :param account_id: account Primary Key
    :return: None
    """
    account = Account.objects.get(id=account_id)
    tweets = utils.fetch_tweets_for_account(account.screen_name)
    for tweet in tweets:
        Tweet.objects.create(account_id=account.id,
                             text=tweet.text)

    logger.info("Successfully Fecthed Tweets for account: ", account)
