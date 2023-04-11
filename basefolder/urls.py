# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

# import paths
from django.urls import path
from .views import indexPageView
from .views import aboutPageView

# url patterns
urlpatterns = [
    path("",indexPageView,name='index'),
    path("about",aboutPageView, name='about'),
]