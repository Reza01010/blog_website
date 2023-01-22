from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_List.as_view(), name='post_list'),
    path('<int:pk>/', views.Post_Detail.as_view(), name='post_detail'),
    path('add/', views.Post_Add.as_view(), name='post_add'),
    path('<int:pk>/update/', views.Post_Update.as_view(), name='post_update'),
    path('<int:pk>/delete/',views.Post_Delete.as_view(), name='post_delete'),
]
