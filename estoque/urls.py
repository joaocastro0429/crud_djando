from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produtos/', views.cadastrar_produtos),
    path('listar_produtos/',views.listar_produtos ,name="listar_produtos"),
    path('deletar_produtos/<int:id>/',views.deletar_produtos,name="deletar_produtos")

    # Add more URL patterns as needed
]

