import classes
import defs

def data_center():
    data=[]             #VAI ARMAZENAR OS DADOS DO USUARIO E PORTANDO SUAS RECEITAS TAMBEM
    while True:
        comand=input(f"""
    Sistema De Cadastro:

        A - Cadastrar usuario
        B - Acessar conta
        C - Alterar dados
        D - Excluir conta
        E - Contas
        
        F - Sair
{"-="*30}
        Resposta: """).upper()


        if comand =="A":
            print("-="*30)
            login=input("Login: ")
            senha=input("Senha: ")
            dia=input("Data: ")
            if len(data)>=1:
                a=""
                for i in range(len(data)):
                    if data[i].login==login:
                        a="S"
                if a=="S":
                    print("Usuário já existente. ")
                else:
                    L=[]                        #CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x=classes.User(login,senha,dia,receita(L,0),0)        
                    data.append(x)
            else:
                L=[]            #SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x=classes.User(login,senha,dia,receita(L,0),0)      
                data.append(x)
            print("-="*30)
            

        elif comand=="B":
            print("-="*30)
            login=input("Login: ")
            senha=input("Senha: ")
            print("-="*30)
            if len (data)>=1:
                for i in data:
                    if i.login==login and i.senha==senha:
                        y=i.contar(1)                       #PARA SABER O NUMERO DE ACESSOS QUE O USUARIO JA FEZ( VAI SER USADO NA FUNCAO   "receita")
                        x=receita(i.user_receita,y) #apos criar uma lista de dicionario e atribuir a "x " 
                        i.user_receita=[]           
                        i.user_receita=x[:]
            else:
                print("Sem dados.")
            print("-="*30)


        elif comand=="C":
            print("-="*30)
            login=input("Login: ")
            senha=input("Senha: ")
            print("-="*30)
            if len (data)>=1:
                for i in data:
                    if i.login==login and i.senha==senha:
                        i.login=input("Novo login: ")
                        i.senha=input("Nova senha: ")
                        print("Dados alterados.")
                    else:
                        print("ERRO. Nao encontrado.")
            else:
                print("Sem dados.")
            print("-="*30)


        elif comand=="D":
            print("-="*30)
            login=input("Login: ")
            senha=input("Senha: ")
            print("-="*30)
            if len (data)>=1:
                for i in data:
                    if i.login==login and i.senha==senha:
                        data.remove(i)
                        print("Dados excluidos.")
                    else:
                        print("ERRO. Nao encontrado.")
            else:
                print("Sem dados.")
            print("-="*30)


        elif comand=="E":
            print("Contas: ")
            if len(data)>=1:
                for i in data:
                    c=i.nome_data()     #usar o metodo da classe User que retorna uma STR 
                    print(c)
            else:
                print("         Não há dados.")
            print("-="*30)


        elif comand=="F":
            break

    return data

def receita(list,y): 
                                                                #herança uso a classe bolo que recebe a classe comida
    l=list
    lista=l[:]      #caso o usuario ja tenha receitas
    if y==0:        # y é o numero de acessos que o usuario fez, para adicionar o Bolo apenas uma vez nao importa a quantidade de logins
        lista.append(classes.Bolo("Bolo","A","B","A","B","B",[{0: ('ovo', '3 unidades')}, {1: ('farinha', '1kg')}, {2: ('leite', '500ml')}, {3: ('fermento', '1 colher se sopa')}],"padrao"))

    while True:
        comando=input(f"""
    {"-="*30}

   ############
   # Receitas #
   ############

        A: Cadastro  
        B: Consultar dados 
        C: Alterar dados 
        D: Mostrar menu de receitas      
        E: Excluir item

        F: Sair

    {"-="*30}
        Resposta: """).upper()

        if comando == "A":
            print("-="*30)
            q,w,e,r,t,y,u=defs.parametros()     #funcao valores
            if len(lista)>=1:
                a=""
                for i in range(len(lista)):
                    if lista[i].nome==q:
                        a="S"
                if a=="S":
                    print()
                    print("Nome já existente. ")
                else:
                    ingre=defs.nomequant(u)           #funcao que retorna uma lista dos ingredientes que vai usar
                    food=classes.Comida(q,w,e,r,t,y,ingre)
                    lista.append(food)
            

        elif comando=="B":
            print("-="*30)
            if len(lista)>=1:
                nome=input("Nome do alimento: ")
                for i in lista:
                    if nome=="Bolo":
                        if i.nome == nome :     #tirei .printar(0)
                            x=i.printar()          #uso de polimorfismo pois objeto Bolo e Comida tem o mesmo metodo   (printar)
                            a=i.retorno()       # metodo que retorna os valorem em forma de lista
                            print(f"""

                            Nome da receita: {a[0]}
                                            {x}

                                                                      Legenda:
                                                {"#"*53}
                                Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
                                Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
                                Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
                                Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
                                Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                                                {"#"*53}

                                    Numero de ingredientes: {len(a[6])} 

                                            Ingredientes: """)
                            for k in range(len(a[6])):
                                print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]}   quantidade: {i.nomequant[k][k][1]}""")
                    else:
                        if i.nome == nome :
                            a=i.retorno()
                            x=i.printar()
                            print(f"""

                            Nome da receita: {x}
                                                                      Legenda:
                                                {"#"*53}
                                Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
                                Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
                                Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
                                Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
                                Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                                                {"#"*53}

                                    Numero de ingredientes: {len(a[6])} 

                                            Ingredientes: """)
                            for k in range(len(a[6])):
                                print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]}   quantidade: {i.nomequant[k][k][1]}""")
            else:
                print("Não há dados.")


        elif comando=="C":
            print("-="*30)
            nome=input("Nome do alimento: ")
            if len(lista)>=1:
                for i in lista:
                    if i.nome==nome:
                        q,w,e,r,t,y,u=defs.parametros()
                        ingre=defs.nomequant(u)
                        lista.remove(i)
                        food=classes.Comida(q,w,e,r,t,y,ingre)
                        lista.append(food)
                    else:
                        print("ERRO. Não encontrado.")
            else:
                print("Não há elementos.")


        elif comando=="D":
            if len(lista)>=1:
                defs.tabela(lista)
            else:
                print("Não há elementos.")


        elif comando=="E":
            if len(lista)>=1:
                deletar=input("Elemento que deseja excluir: ")
                for i in lista:
                    if i.nome==deletar:
                        lista.remove(i)
                        print("Item excluído.")
                    #else:
                        #print("ERRO. Não encontrado.")                  printa erro toda vez que um elemento da lista tem i.nome diferente do deletar,
            else:                                                       # assim como em outros "for" por isso tirei a maioria desses print()
                print("Não há elementos.")


        elif comando == "F":
            break
    return lista


data_center()