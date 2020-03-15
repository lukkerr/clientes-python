def funclistar():
    import funcoes
    #Abrir Arquivo no Modo Leitura
    arq = open("clientes.txt","r")
    #Pegar todo o Texto do Arquivo e Converte-lo em Lista, sendo Cada Linha um Elemento da Lista
    arqtexto = arq.readlines()
    #Listar - Retorna uma Lista com Todos os Usuários Cadastrados, Formatados parar o Print
    arqtexto = funcoes.listar(arqtexto)
    print("-------------------------------Usuários-------------------------------\n")
    #Print Cada Linha de Usuário feito pela Função Listar
    for i in arqtexto:
        print(i)
    print("----------------------------------------------------------------------\n")
    #Conta o Numero de Elementos da Lista Criada, Consequentemente o Numero de Clientes
    print("Total de Clientes: ",len(arqtexto))
    #Fecha Arquivo Aberto no Modo Leitura
    arq.close()