def funcexcluir():
    import funcoes
    while True:
        cpf = int(input("Digite CPF (Só 11 Números): "))
        cpf = str(cpf)
        #Sair se CPF Igual a Zero
        if cpf == "0":
            print("\n")
            break
        #Abrir Arquivo no Modo de Leitura
        arq = open("clientes.txt","r")
        #Adicionar todo Texto do Arquivo na Variavel Arqtexto
        arqtexto = arq.read()
        #Fechar Arquivo Aberto no Modo Leitura
        arq.close()
        #Cpffind - Verificar se CPF é Valido
        cpffind = funcoes.validador(arqtexto,cpf)
        #Cpffind Retorna True se CPF esta contido no texto do Arquivo
        if cpffind == True:
            #Abrir arquivo no Modo Leitura
            arq = open("clientes.txt","r")
            #Converter Texto no Arquivo em uma Lista, sendo cada Linha do Arquivo um Elemento
            arqtexto = arq.readlines()
            #Função Excluirelemento - Retorna uma String do Texto Original, porém com sem a Linha do Usuário Exluido
            arqtexto = funcoes.excluirelemento(arqtexto,cpf)
            #Fechar Arquivo que estava aberto no Modo Leitura
            arq.close()
            #Sair do Laço
            break
        #Se Cpffind não Encontrar o CPF fica preso no Laço
        else:
            print("\n---CPF não Cadastrado---\n")
    #Só Executar Instrução se CPF Informado acima for Diferente de Zero
    if cpf != "0":    
        #Abrir arquivo no Modo Escrita
        arq = open("clientes.txt","w")
        #Escrever Texto no arquivo Arqtexto, já com linha do Usuário selecionado excluida
        arq.write(arqtexto)
        #Fechar Arquivo que estava aberto no Modo Escrita
        arq.close()
        print("\n---Finalizado com Sucesso---")