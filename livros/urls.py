from django.urls import path
from .views import LivroListCreate, LivroDetail

urlpatterns = [
    path('livros/', LivroListCreate.as_view(), name='livro-list-create'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
]
