from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include

from .views import (
    DashboardView,
    GastroUpdateView,
    HomeView,
    GastroNewView,
    ApiGastroLocationsJson,
    GastroDeleteView,
    GastroSubmitView,
    GastroSubmitListView,
    GastroSubmitEditView,
    GastrosClosedView,
    GastroSubmitDeleteView,
    UserProfileView,
    UserPasswordChangeView, DataAuthView)

app_name = 'data'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/GastroLocations.json', ApiGastroLocationsJson.as_view(), name='api'),

    # listviews
    # open
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #closed
    path('gastros-closed/', GastrosClosedView.as_view(), name='gastros-closed'),

    path('gastro-new/', GastroNewView.as_view(), name='gastro-new'),
    path('location/gastro/<str:id_string>/edit/', GastroUpdateView.as_view(), name='gastro-update'),
    path('location/gastro/<str:id_string>/delete/', GastroDeleteView.as_view(), name='gastro-delete'),

    path('gastro-submit-list/', GastroSubmitListView.as_view(), name='gastro-submit-list'),
    path('gastro-submit/<int:pk>/edit/', GastroSubmitEditView.as_view(), name='gastro-submit-edit'),
    path('gastro-submit/<int:pk>/delete/', GastroSubmitDeleteView.as_view(), name='gastro-submit-delete'),

    # public
    path('gastro-submit/', GastroSubmitView.as_view(), name='gastro-submit'),

    # auth urls
    path('accounts/login/', DataAuthView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('accounts/user/profile/change-password/', UserPasswordChangeView.as_view(), name='user-profile-change-password'),
]
