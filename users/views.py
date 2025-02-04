"""Views."""

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

# from django.core.exceptions import PermissionDenied
from .models import CustomUser


class CustomUserListView(LoginRequiredMixin, ListView):
    """UserListView."""

    model = CustomUser
    template_name = "customuser_list.html"
    login_url = "login"

    def get_queryset(self):
        """Get query set."""
        return CustomUser.objects.order_by("last_name", "first_name")


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    """UserDetailView."""

    model = CustomUser
    template_name = "customuser_detail.html"
    login_url = "login"


class CustomUserUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):
    """UserUpdateView."""

    model = CustomUser
    template_name = "customuser_update.html"
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "shifts_per_roster",
        "enforce_shifts_per_roster",
        "enforce_one_shift_per_day",
        "max_shifts",
        "available",
        "roles",
    )
    login_url = "login"
    permission_required = "rosters.change_roster"


class CustomUserDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    """UserDeleteView."""

    model = CustomUser
    template_name = "customuser_delete.html"
    success_url = reverse_lazy("customuser_list")
    login_url = "login"
    permission_required = "rosters.change_roster"


class CustomUserCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    """UserCreateView."""

    model = CustomUser
    template_name = "customuser_create.html"
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "shifts_per_roster",
        "enforce_shifts_per_roster",
        "enforce_one_shift_per_day",
        "max_shifts",
        "available",
        "roles",
    )
    login_url = "login"
    permission_required = "rosters.change_roster"
