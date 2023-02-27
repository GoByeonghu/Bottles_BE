from django.urls import path
from app import views

urlpatterns = [
    path('app/', views.user_list),
    path('user/register/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user/read/', views.ReadProfileView.as_view()),
    path('user/update/', views.UpdateProfileView.as_view),
    path('user/delete/', views.DeleteProfileView.as_view),
]