from django.conf.urls import url, include
from django.contrib import admin

import stats.urls_rest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(stats.urls_rest)),
]