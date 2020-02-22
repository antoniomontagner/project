class Comida:
    def __init__ (self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant):
        self.nome=nome
        self.doce_salgado=doce_salgado
        self.star=star
        self.hot_cold=hot_cold
        self.temp=temp
        self.porc=porc
        self.nomequant=nomequant
    def retorno (self):
        return self.nome,self.doce_salgado,self.star,self.hot_cold,self.temp,self.porc,self.nomequant
    def printar(self):
        return self.nome                                         #polimorfismo com Bolo.printar


class Bolo(Comida):             #heranca
    def __init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant,r_padrao):
            Comida.__init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant)
            self.r_padrao=r_padrao
    def printar(self):
        #self.x=x
        return "A receita de bolo vem de bonus."                # tirei o "X"  polimorfismo  tem que tirar o parametro "X" pois nao precis

class User:
    def __init__(self,login,senha,data,user_receita,cont):
        self.login=login
        self.senha=senha
        self.data=data
        self.user_receita=user_receita 
        self.cont=cont
    def contar(self,contar):
        self.cont+=contar
        return self.cont
    def nome_data(self):
        return f"""{"":10} User: {self.login}     Data de login: {self.data}"""