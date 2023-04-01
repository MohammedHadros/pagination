from django.urls import path
from .views import *

urlpatterns = [
    path("" ,AllKeywordsView.as_view()  ),
    path("list" ,KeywordListView.as_view()  ),
    #path("list/<int:page>" ,KeywordListView.as_view()  ),
    path("list/<int:page>" ,listing , name="listing" ),
    path("terms.json",listing_api,name="terms-api"),
    path("faux",AllKeywordsView.as_view(template_name="terms/faux_pagination.html")),

] 