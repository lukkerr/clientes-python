def funcpesquisar():
    import funcoes
    #While 1
    while True:
        #While 2
        while True:
            cpf = int(input("Digite CPF (Só 11 Números): "))
            cpf = str(cpf)
            #Sair do While 2 se CPF Igual a Zero
            if cpf == "0":
                break
            #Abrir Arquivo no Modo Leitura
            arq = open("clientes.txt","r")
            #Arqtexto Passa a ter todo conteúdo do Arquivo
            arqtexto = arq.read()
            #Fechar arquivo
            arq.close()
            #Validar - Verifica se numero do CPF esta Presente no texto Dado
            cpffind = funcoes.validador(arqtexto,cpf)
            #Validador Retorna True se não for Encontrado
            if cpffind == True:
                #Abrir Arquivo no Modo Leitura
                arq = open("clientes.txt","r")
                #Arqtexto Passa a ter todo conteúdo do Arquivo como Lista, e cada linha do texto agora é um Elemento na Lista
                arqtexto = arq.readlines()
                #Chamando a Função Pesquisar - Que Retorna String com todos os Dados do cliente já Formatados
                arqtexto = funcoes.pesquisar(arqtexto,cpf)
                #Fechar Arquivo
                arq.close()
                #Sair do While 2
                break
            else:
                print("\n---CPF não Cadastrado---\n")
        #Ao Chegar nesse Ponto o Programa esta de volta ao While 1
        #Sair do While 1 se CPF Igual a Zero
        if cpf=="0":
            break
        else:
        #Se for Diferente de Zero
            print("\n",arqtexto,)
            ident = ""
            #While 2 - Repetir Pergunta até dizer S/N
            while True:
                ident = input("Deseja Pesquisar Novamente (S/N): ")
                ident = ident.lower()
                #Se digitar n/N sair do While 2 
                if ident=="n":
                    break
                #Se digitar s/S sair do While 2
                elif ident=="s":
                    break
                #Se digitar outro Valor fica preso no Laço
                else:
                    print("\n---Opção Inválida---\n")
            #Se Valor Anterior Igual a n/N sair de While 1
            if ident=="n":
                break