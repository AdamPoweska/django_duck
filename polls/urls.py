from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.results, name="results"),
    # duck dropdown list
    path('duck-selector/', views.home_view, name="duck_selector"),
    # duck rating dropdown list
    path('duck-rating/', views.home_rating, name="ducks_rating"),
]
