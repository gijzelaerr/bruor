from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from braces.views import LoginRequiredMixin
from .models import Recipe


class OverView(TemplateView):
    template_name = 'recipe/overview.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe


class PublicRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return super().get_queryset().filter(public=True)


class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'public']


class ReciperUpdate(UpdateView):
    model = Recipe


class RecipeDelete(DeleteView):
    model = Recipe
