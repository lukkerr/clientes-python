#1 - Arquivo Python com a Funcão de Cadastro
import cadastrar
#2 - Arquivo Python com a Funcão de Pesquisar
import pesquisar
#3 - Arquivo Python com a Funcão de Editar
import editar
#4 - Arquivo Python com a Funcão de Excluir
import excluir
#5 - Arquivo Python com a Funcão de Listar
import listar 
#Modulo usado para Verificar Existência do Arquivo
import os.path
#Criar Lista de Clientes caso não Exista
if (os.path.isfile("clientes.txt"))==False:
    arq = open("clientes.txt","w")
    arq.close()
while True:
    print("\n")
    print("------------------------------------------------")
    print("--------Escolha uma das Opções a Seguir---------")
    print("------------------------------------------------\n")
    print("[1] Cadastrar usuário")
    print("[2] Pesquisar usuário")
    print("[3] Alterar usuário")
    print("[4] Excluir usuário")
    print("[5] Listar usuários")
    print("[0] Sair/Voltar\n")
    op = int(input("Selecione uma Opção: "))
    print("\n")
    if op==1:
        cadastrar.funccadastrar()
    elif op==2:
        pesquisar.funcpesquisar()
    elif op==3:
        editar.funceditar()
    elif op==4:
        excluir.funcexcluir()
    elif op==5:
        listar.funclistar()
    elif op==0:
        break
    else:
        print("\n---Opção Invalída---\n")