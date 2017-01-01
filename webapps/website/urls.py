from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', view=views.LandingPageView.as_view(), name="home")
]