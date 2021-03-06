from django.conf import settings
from django.conf.urls.static import static

from lists import views as list_views
from lists import urls as list_urls
from accounts import urls as account_urls
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^accounts/', include(account_urls)),
]
