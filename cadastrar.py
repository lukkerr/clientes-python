def funccadastrar():
    import funcoes
    nome = input("Digite o seu Nome: ")
    #While 1
    while True:
        cpf = int(input("Digite CPF (Só 11 Números): "))
        cpf = str(cpf)
        #Sair de While 1 se CPF Igual a Zero
        if cpf == "0":
            print("\n")
            break
        #Abrir Arquivo no Modo Leitura
        arq = open("clientes.txt","r")
        #Arqtexto Passa a ter todo conteúdo do Arquivo
        arqtexto = arq.read()
        #Validar se numero do CPF esta Presente no texto Dado
        cpffind = funcoes.validador(arqtexto,cpf)
        #Validador Retorna True se não for Encontrado
        if cpffind==False:
            dominio = "ifnet.com.br"
            #Divisionuser - Separa o Nome dado, pelos "Espaços em Branco" e os Retorna em Lista
            listanome = funcoes.divisionuser(nome)
            #Emailconstruct - Usa a Lista com os Nomes,Junto com CPF e Dominio Padrão para Gerar Emails dentro de uma Lista
            emails = funcoes.emailconstruct(listanome,cpf,dominio)
            #While 2
            while True:
                #While 3
                while True:
                    print("Escolha uma das Opções de Email")
                    #Alternativas de Emails
                    print("1 -",emails[0])
                    print("2 -",emails[1])
                    print("3 -",emails[2])
                    email = int(input("Digite a Opção: "))
                    #Se Digitar 1, Sair do While 3
                    if email==1:
                        email = emails[0]
                        break
                    #Se Digitar 2, Sair do While 3
                    elif email==2:
                        email = emails[1]
                        break
                    #Se Digitar 3, Sair do While 3
                    elif email==3:
                        email = emails[2]
                        break
                    #Se Digitar outro Valor fica Preso no Laço
                    else:
                        print("Reveja a Escolha de Email")
                #Ao Chegar nesse Ponto o Programa esta de volta ao While 2
                #Validador - Verifica se Email Escolhindo esta Disponível
                valiemail = funcoes.validador(arqtexto,email)
                #Validador Retorna False se email Disponível
                if valiemail==False:
                    #Sair do While 2
                    break
                #Se Email não estiver Disponível fica Preso no Laço
                else:
                    print("\n---Email já Cadastrado---\n")
            #Ao Chegar nesse Ponto o Programa esta de volta ao While 1
            #Construindo Linha do Usuário no Arquivo de Texto
            cadastro = cpf +";"+ nome +";"+ email + "\n"
            #Abrir Arquivo no Modo de Adição
            arq = open("clientes.txt","a")
            #Escrevendo Texto da Variavel Cadastro no Arquivo
            arq.write(cadastro)
            #Fechando Arquivo
            arq.close()
            print("\n---Finalizado com Sucesso---")
            #Sair do While 1
            break
        #Se CPF Digitado, já estiver Cadastrado, fica Preso no Laço
        else:
            print("\n---CPF já Cadastrado---\n")