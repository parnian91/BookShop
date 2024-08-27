from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('books', views.BookViewSet)
router.register('buyers', views.BuyerViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('authors/<int:pk>/publisher-books/', views.publisher_books, name='publisher-books'),
]


# path(r'^authors/', views.AuthorList.as_view(), name='authorList'),
# path(r'^authors/<int:pk>', views.AuthorDetail.as_view(), name='authorDetail'),
# path('users/', views.UserList.as_view()),
# path('users/<int:pk>', views.UserDetail.as_view()),