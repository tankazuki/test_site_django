from django.urls import path
from . import views

app_name = 'app01'

urlpatterns = [
    path('', views.ListMemoView.as_view(), name='index'),
    path('memo/<int:pk>/', views.DetailMemoView.as_view(), name='detail'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]