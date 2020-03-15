###Testar se Existe determinado Contéudo no Texto###
def validador (arqtexto,x):
    #Find - Procura Contéudo da Varíavel X no Arqtexto e Retorna sua Posição
    resultado = arqtexto.find(x)
    #Resultado Igual a -1 se Contéudo não for Encontrado no Texto
    if resultado==-1:
        resultado = False
    #Se Diferente de -1 o Contéudo foi encontrado no Texto
    else:
        resultado = True
    #Retorna Valor True se Contéudo foi Encontrado, e False se não
    return resultado

###Dividir o Nome do Usuário para fazer o Email###
def divisionuser (nome):
    #Converte todo o Nome dado para Mínusculo
    nome = nome.lower()
    #Separa o Nome dado, retornando o como uma Lista (sendo "Espaço em Branco" o Valor Default para a Divisão)
    resultado = nome.split()
    #Retorna uma Lista com o Nome Dividido onde havia "Espaços em Branco"
    return resultado
    
###Gerar Opcoes de Emails###
def emailconstruct (nome,cpf,dominio):
    #Construindo Email com Nome do Cliente (Sendo Nome uma Lista feita com o Divisionuser User Acima), CPF e Dominio Padrão
    #Construindo Alternativa de Email 1
    mail1 = cpf + "@" + dominio
    #Construindo Alternativa de Email 2
    mail2 = nome[0] +"."+ nome[-1] + "@" + dominio
    #Construindo Alternativa de Email 3
    mail3 = nome[0] +"."+ cpf[0:3] + "@" + dominio
    #Resultado vai ser uma lista com todos as Alternativas de Email
    resultado = [mail1,mail2,mail3]
    #Retorna um Lista de Emails
    return resultado

####Editar Lista###
def editarlista (lista,conteudo):
    #Lembrando que a lista dada todos os Usuário sendo cada elemento uma linha de Dados daquele Usuário
    #Retorna a Quantidade de Linhas da Lista Dada
    cont = len(lista)
    #Percorrer o Numero equivalente ao numero de elemento da Lista
    for i in range(cont):
        #Entrar no If se o contéudo for Encontrado naquele elemento da Lista
        if lista[i].find(conteudo)!=-1:
            #Deve-se Dividir a Lista contando como Separador o ";",salvando o resultado em uma nova Lista
            listacop = lista[i].split(";")
            #Salvando Localização daquele Elemento na lista Original
            loc = i
    #Mudando o Texto do Espaço do Nome do Cliente
    listacop[1] = input("Digite o Novo Nome a ser Adicionado: ")
    #A Posição do Elemento Encontrado Anteriormente vai ser Sobreescrito, porém com o "listacop[1]" Alterado ou seja o Nome
    lista[loc] = listacop[0] +";"+ listacop[1] +";"+ listacop[2]
    #Declarando Variável String
    listanova = ""
    #Convertendo todo o Texto da Nova Lista Alterada em uma String
    for i in lista:
        #Cada Linha esta sendo adicionada em uma String
        listanova = listanova + i
    #Retorna Todo Texto da Lista dada Anteriormente, porém agora como String e com Nome Especificado Alterado
    return listanova

###Separar Dados de Usúarios por Elemento na Lista###
def splitelemento (listageral,ident):
    #Retorna a Quantidade de Linhas da Lista Dada
    cont = len(listageral)
    #Percorrer o Numero equivalente ao numero de elemento da Lista
    for i in range(cont):
        #Entrar no If se o contéudo for Encontrado naquele elemento da Lista
        if listageral[i].find(ident)!=-1:
            #Deve-se Dividir a Lista contando como Separador o ";",salvando o resultado em uma nova Lista
            identsplit = listageral[i].split(";")
    #Retorna uma Lista com o Contéudo da Linha do Elemento Procurado
    return identsplit

###Exluir Usuário###
def excluirelemento (listaex,elemento):
    #Retorna a Quantidade de Linhas da Lista Dada
    cont = len(listaex)
    #Retorna uma Lista com o Contéudo da Linha do Elemento Procurado
    listacopex = splitelemento(listaex,elemento)
    while True:
        #A Variável Listacopex Retorna os Valores de CPF, Nome e Emails, separados pela função Splitelemento
        print("---Cliente a ser Deletado---\n")
        print("CPF:  ",listacopex[0])
        print("Nome: ",listacopex[1])
        print("Email:",listacopex[2])
        select = input("Deseja Realmente Deletar Usuário (S/N): ")
        #Converte a Resposta dada para Minusculo
        select = select.lower()
        #Cria Variável com String
        listanovaex = ""
        #Entra no IF se digitou s/S
        if select=="s":
            #Laço com Quantidade de Giros Equivalente ao Numero de Elementos Lista "Original"
            for i in range(cont):
                #Ao Encontrar Linha do Usúario com Elemento Dado, entrar no IF
                if listaex[i].find(elemento)!=-1:
                    #Substituir todo o Valor da Linha do Usuário por "Nada" 
                    listaex[i] = ""
        #Entrar no IF se a Respota foi Valida
        if select=="s" or select=="n":
            #Percorrer a Lista Original, que agora esta com a Linha do Elemento Dado Apagada
            for i in listaex:
                #Adicionando Elementos todos os Elementos da Lista em uma String
                listanovaex = listanovaex + i
            #Sair do Laço
            break
        #Se Digitar qualquer Valor Diferente de s/S ou n/N, fica preso no Laço
        else:
            print("\n---Opção Inválida---\n\n")
    #Retorna String com todo o Texto, sendo que com a Linha do Elemento Contido Apagada se tiver Digitado s/S
    return listanovaex

###Pesquisar Usuário###
def pesquisar(listapes,cpf):
    #Retorna uma Lista com o Contéudo da Linha do Elemento Procurado
    user = splitelemento(listapes,cpf)
    #Retorna a Quantidade de Linhas da Lista Dada
    cont = len(user)
    #Texto que Ficaram a Frente dos Dados
    idenc = [" CPF: "," Nome: ","Email: "]
    #Lista de Espaços para Formatação
    pulalinha = ["\n","\n",""]
    #Criando Variavel String
    userprint = ""
    #Entrando em Laço de 3, por serem 3 Linhas cada Dado CPF, Nome e Email
    for i in range(3):
        #Salva uma Linha com Cada Dado com seus Respectivos Dados de Formatação e salva todos em uma String
        userprint = userprint + idenc[i] + user[i] + pulalinha[i]
    #Retorna uma String com todos os Valores prontos pra Print
    return userprint

###Gerar Lista Vazio###
def listavazia(x,y):
    #Laço para Preencher a Lista "X" com uma Quantidade "Y" de Valores
    for i in range(y):
        x.append("0")
    #Retorna uma Lista com uma Quantidade "Y" de Zeros
    return x

###Listar Usuários###
def listar(users):
    #Retorna a Quantidade de Linhas da Lista Dada
    cont = len(users)
    #Criando Lista Vazio
    userslista = []
    #Função Listavazia - Retorna um Lista "Vazia" (Zerada) com o Mesmo Numero de Elementos da Lista Dada Originalmente nesta Função
    userslista = listavazia(userslista,cont)
    #Percorrer o Numero equivalente ao numero de elemento da Lista
    for i in range(cont):
        #Divide todos os Elementos da Lista onde Existe ";", gerando uma Lista de Listas
        userslista[i] = users[i].split(";")
    #Criando Lista Vazia
    usersfinal = []
    #Função Listavazia - Retorna um Lista "Vazia" (Zerada) com o Mesmo Numero de Elementos da Lista Dada Originalmente nesta Função
    usersfinal = listavazia(usersfinal,cont)
    #Lista com Texto de Formatação que Ficaram a Frente dos Dados
    idenc = ["CPF: ","Nome: ","Email: "]
    #Percorrer o Numero equivalente ao numero de elemento da Lista
    for i in range(cont):
        #Adicionando Cada Linha da Lista Original a uma Unica Linha da Lista Final, estando agr Formatada
            #(Sendo Cada Elemento da Nova Lista um Cliente)
        usersfinal[i] = str(i+1) +" - "+ idenc[0] + userslista[i][0] + " | " + idenc[1] + userslista[i][1] + " | " + idenc[2] + userslista[i][2]
    #Retorna Lista com Todos os Clientes e já Formatado, sendo cada elemento os dados de um único Cliente
    return usersfinal