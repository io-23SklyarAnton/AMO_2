from django.urls import path
from . import views

app_name = 'algorithms'

urlpatterns = [
    path('multiple_lists/', views.MultipleListsView.as_view(), name='multiple_lists'),
    path('concrete_list/', views.ConcreteListView.as_view(), name='concrete_list'),
    path('home/', views.home_view, name='home')
]
