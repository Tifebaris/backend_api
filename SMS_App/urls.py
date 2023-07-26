from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken



urlpatterns=[
    path('course/', views.CourseListView.as_view(), name='course'),
    path('students/', views.StudentApiView.as_view(), name='student'),
    path('instructor/', views.InstructorApiView.as_view(), name='instructor'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('token_login/', obtain_auth_token, name='token_login'), 
    # path('user/', views.CreateNewUser.as_view(), name='new_user'), 
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course'),
    path('students/<int:pk>/', views.StudentApiView.as_view(), name='student')
]