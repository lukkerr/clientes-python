def funceditar():
    import funcoes
    while True:
        cpf = int(input("Digite CPF (Só 11 Números): "))
        cpf = str(cpf)
        #Sair do Laço se CPF Igual a Zero
        if cpf == "0":
            print("\n")
            break
        #Abrir arquivo no Modo Leitura
        arq = open("clientes.txt","r")
        #Adicionar todo Texto do Arquivo na Variavel Arqtexto
        arqtexto = arq.read()
        #Fechar Arquivo que estava no Modo Leitura
        arq.close()
        #Validador - Validar se CPF digitado é encontrado no Texto do Arquivo, Salvo na Variavel Arqtexto
        cpffind = funcoes.validador(arqtexto,cpf)
        #Cpffind - Retorna True se CPF já Existe
        if cpffind == True:
            #Abrir Arquivo no Modo Leitura
            arq = open("clientes.txt","r")
            #Arqtexto agora possui todo texto do Arquivo, porém como Lista, sendo cada Linha um Elemento
            arqtexto = arq.readlines()
            #Função Editarlista - Retorna uma String com Todo o Texto, sendo que com o Nome do CPF informado Alterado
            arqtexto = funcoes.editarlista(arqtexto,cpf)
            #Fechar Arquivo no Modo Leitura
            arq.close()
            #Sair do Laço
            break
        #Se Cpffind não Encontrar CPF fica Preso no Laço
        else:
            print("\n---CPF não Cadastrado---\n")
    #Só Executar Instrução se CPF Informado no Inicio Diferente de 0
    if cpf != "0":
        #Abri Arquivo agr no Modo de Escrita    
        arq = open("clientes.txt","w")
        #Escrevendo Texto Alterado da Variavel Arqtexto na Variavel
        arq.write(arqtexto)
        #Fechar Arquivo que estava Aberto no modo Escrita
        arq.close()
        print("\n---Nome Alterado com Sucesso---")