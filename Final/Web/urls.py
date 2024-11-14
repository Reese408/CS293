from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('pools', views.pools, name="pools"),
    path('quote', views.quote, name="quote"),
    path('construction', views.construction, name="construction"),
    path('submit_form', views.submit_form, name='submit_form'),
    path('submitted', views.quote_request_view, name="quote_request"),
]
