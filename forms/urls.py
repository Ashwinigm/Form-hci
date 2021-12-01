from django.contrib import admin
from django.urls import path
from formapp import views
from formapp.views import AddView, HomeView, SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.show),
    path('show/',views.search_show),
    path('', views.my_form, name='add'),
    path('home/', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]