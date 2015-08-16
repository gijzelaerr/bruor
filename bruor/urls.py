from django.conf.urls import include, url
from django.contrib import admin

from recipe.views import RecipeDetailView, UserRecipeListView, PublicRecipeListView,  RecipeCreate, ReciperUpdate,\
    RecipeDelete, OverView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$', OverView.as_view(), name='overview'),
    url(r'^recipe/(?P<pk>\d+)/$', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^recipe/list/$', UserRecipeListView.as_view(), name='user_recipe_list'),
    url(r'^recipe/publist/$', PublicRecipeListView.as_view(), name='public_recipe_list'),
    url(r'^recipe/add/$', RecipeCreate.as_view(), name='recipe_add'),
    url(r'^recipe/update/(?P<pk>\d+)/$', ReciperUpdate.as_view(), name='recipe_update'),
    url(r'^recipe/delete/(?P<pk>\d+)/$', RecipeDelete.as_view(), name='recipe_delete'),


    # authentication
    url('^accounts/', include('django.contrib.auth.urls')),
]
