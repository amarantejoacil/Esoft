from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('consultarcep',views.IndexView, name='consultarcep'),
    path('cadastrar/', views.CadastrarEndereco, name='cadastrar-endereco'),
    # path('atualizar/<int:pk>/', views.AtualizarEndereco, name='atualizar-endereco'),
    path('deletar/<int:pk>/', views.DeletarEndereco, name='deletar-endereco'),
]