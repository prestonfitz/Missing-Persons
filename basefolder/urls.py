# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

# import paths
from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import showPageView

# url patterns
urlpatterns = [
    path("/about",aboutPageView, name='about'),
    path("<int:id>/", showPageView, name= 'showmissing'),
    path("",indexPageView,name='index'),
]