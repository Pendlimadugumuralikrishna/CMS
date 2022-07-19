from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView



from django.contrib.auth.views import LoginView


urlpatterns = [ 
    path("",views.indexview,name = "home"),
    path("packages/",views.package_detail,name = "packages"),
    path("dashboard/",views.dashboardview,name="dashboard"),
    path("login/",LoginView.as_view(),name="Login_url"),
    path("register/",views.registerview,name="register_url"),
    path("logout/",LogoutView.as_view(next_page = 'dashboard'),name="logout"),
    path("package/",views.all_packages,name="user_package")
]
