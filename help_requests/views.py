from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import HelpRequest


class HelpRequestListView(ListView):
    model = HelpRequest
    template_name = "help_requests/request_list.html"
    context_object_name = "help_requests"
    ordering = ["-created_at"]

    def get_queryset(self):
        return HelpRequest.objects.filter(status="open").order_by("-created_at")


class HelpRequestDetailView(DetailView):
    model = HelpRequest
    template_name = "help_requests/request_detail.html"
    context_object_name = "help_request"


class HelpRequestCreateView(LoginRequiredMixin, CreateView):
    model = HelpRequest
    fields = [
        "title",
        "description",
        "category",
        "start_location",
        "end_location",
        "is_paid",
        "payment_note",
    ]
    template_name = "help_requests/request_form.html"
    success_url = reverse_lazy("help_requests:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
