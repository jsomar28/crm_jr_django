from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SecureLoginView, UserListView, DashboardView
from .views import SignupView, SecureLogoutView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', SecureLoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('users/', UserListView.as_view(), name='user_list'),

]
