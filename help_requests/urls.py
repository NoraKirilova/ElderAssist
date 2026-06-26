from django.urls import path
from .views import HelpRequestListView, HelpRequestDetailView, HelpRequestCreateView

app_name = "help_requests"

urlpatterns = [
    path("", HelpRequestListView.as_view(), name="list"),
    path("new/", HelpRequestCreateView.as_view(), name="create"),
    path("<int:pk>/", HelpRequestDetailView.as_view(), name="detail"),
]