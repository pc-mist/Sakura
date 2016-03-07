from django.conf.urls import url
from .views import LoginFormView, LogoutView, IndexView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^$', IndexView.as_view()),
]