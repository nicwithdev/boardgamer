from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('games/', views.games_index, name="index"),
    path('games/<int:game_id>/', views.games_detail, name="detail"),
    path('create/', views.create, name="create"),
    path('create/submit/', views.submit_create),
    path('games/<int:game_id>/edit/', views.edit, name="edit"),
    path('games/<int:game_id>/update/', views.update),
    path('games/<int:game_id>/delete/', views.delete),
    path('games/<int:game_id>/add_review/', views.review_form),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/user/', views.my_games),
    path('games/search/', views.render_search),
]
