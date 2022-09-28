from Rest_API_Models import Pessoas,Atividades,Usuarios

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Demetrio',idade=40)
    print(pessoa)
    pessoa.save()
def insere_atividades():
    atividade = Atividades(nome='UX DESIGN')
    print(atividade)
    atividade.save()
def insere_usuarios(login, senha):
    usuarios = Usuarios(login=login, senha=senha)
    usuarios.save()
#Consulta a tebela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Julia').first()
    print(pessoa.nome)
def consulta_atividades():
    atividade= Atividades.query.all()
    print(atividade)
def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
#Altera informações na tabela pessoa
def altera_pessoa():
    pessoa =  Pessoas.query.filter_by(nome='Julia').first()  
    pessoa.nome = 'Felipe'
    pessoa.save()
#Exclui alguma informação da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()
    print('0')
if __name__ == '__main__':
   #insere_usuarios('sergio','1234')
   #insere_usuarios('patricia','4321')
    #consulta_usuarios()
    #insere_pessoas()
    #insere_atividades()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
    consulta_atividades()