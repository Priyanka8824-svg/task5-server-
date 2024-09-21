from django.urls import path
from .views import (SignInView, SignUpView, UserTasksView, UserInfoView, LogoutView,
                    ListAPIView, CookieTokenRefreshView, AccountActivationView, UserTasksView)

urlpatterns=[
    path('signin/', SignInView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('user/info/', UserInfoView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('refresh/', CookieTokenRefreshView.as_view()),

    path('account/activate/<token>/', AccountActivationView.as_view()),
    path('user/tasks/<pk>/', UserTasksView.as_view())
]