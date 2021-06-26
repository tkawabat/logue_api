from django.urls import path
from . import views

urlpatterns = [
    path('scenario/', views.ScenarioList.as_view()),
    path('scenario/<int:id>/', views.ScenarioDetail.as_view()),
    # path('user/<int:pk>/', views.User.as_view()), #1日の詳細
    # path('<str:cat>/', views.CategoryDairy.as_view()), #カテゴリ別一覧
]