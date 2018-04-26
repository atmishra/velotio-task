from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from mytweepy.core.views import AccountListCreateView, TweetListView

urlpatterns = [
                  url(r'^api/v1/accounts$',
                      AccountListCreateView.as_view(),
                      name='ListCreateAccounts'),

                  url(r'^api/v1/accounts/(?P<account_id>\d+)/tweets$',
                      TweetListView.as_view(),
                      name='ListTweets'),

                  url(r'^admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
