from django.conf.urls import url



urlpatterns = [
    url(r'^$', 'catalog.views.index', name='index'),
]