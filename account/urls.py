from django.urls import include, path

from . import views

app_name = "account"

urlpatterns = [
    path("crsf", views.get_crsf, name="api-crsf")
]

# router.register(r"crsf", views.SetCrsfToken, basename="crsf")
# router.register(r"login", views.LoginViewSet, basename="login")
# router.register(r"whoami", views.WhoamiViewSet, basename="whoami")
