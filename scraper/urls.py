from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('scrape/', views.run_scraper),
    path('quotes/', views.get_quotes),
    path('dashboard/', views.dashboard),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
]