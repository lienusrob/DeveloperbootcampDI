from django.urls import path, include
from profile_app.views import UserListView, UserDetailView


urlpatterns = [
    path ('profile_list/', UserListView.as_view(), name= 'profile_list'),
    path ('profile_detail/<int:pk>/', UserDetailView.as_view(), name= 'profile_detail')

]