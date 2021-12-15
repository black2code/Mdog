from django.urls        import path
from django.urls.resolvers import URLPattern
from owners import views
from owners.models import dog

from owners.views   import  ownersView, dogsView

urlpatterns = [
    path('owners', ownersView.as_view()),
    path('dogs', dogsView.as_view())
]