from django.urls import include, path

from . import views

app_name = "account"

urlpatterns = [
    path("crsf/", views.get_crsf, name="api-crsf"),
    path("login/", views.login_view, name="api-login"),
    path("logout/", views.logout_view, name="api-logout"),
    path('session/', views.SessionView.as_view(), name='api-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
]

# router.register(r"crsf", views.SetCrsfToken, basename="crsf")
# router.register(r"login", views.LoginViewSet, basename="login")
# router.register(r"whoami", views.WhoamiViewSet, basename="whoami")
