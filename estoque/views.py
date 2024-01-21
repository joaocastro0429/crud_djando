from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Produto

# Create your views here.


def cadastrar_produtos(request):
      if request.method=="GET":
        return render(request,'cadastrar_produtos.html')
      elif request.method=="POST":
          nome1=request.POST.get('nome')
          preco1=request.POST.get('preco')
          validade1=request.POST.get('validade')
          quantidade1=request.POST.get('quantidade')

          produto=Produto(
           nome=nome1,
           preco=preco1,
           validade=validade1,
           quantidade=quantidade1

        )
      produto.save()
      return redirect('/estoque/cadastrar_produtos')

def listar_produtos(request):
    produto= Produto.objects.all()
    id = request.GET.get('preco')
  
    if id:
       produto = produto.filter(id=id)
    
    return render(request, 'listar_produtos.html', {'produto': produto})



def deletar_produtos(request,id):
# Suponha que você tenha um objeto Produto com o id 1 que deseja excluir
 produto_para_excluir = Produto.objects.get(id=id)
 produto_para_excluir.delete()
 return redirect("/estoque/listar_produtos/")
