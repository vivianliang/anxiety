from django.conf.urls import url

from core.views import AnxietyView, AnxietiesView

urlpatterns = [
    url(r'^anxiety/(?P<anxiety_id>[0-9]+)/$', AnxietyView.as_view()),
    url(r'^anxieties/$', AnxietiesView.as_view()),
]
