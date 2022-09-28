from flask import Flask, request
from flask_restful import Resource, Api
from Rest_API_Models import Pessoas,Atividades,Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#   'Augusto':'123',
#    'julia':'321'
#}
#@auth.verify_password
#def verificacao(login, senha):
#    print('validando usuario')
#    print(USUARIOS.get(login) == senha)
#    if not (login, senha):
#        return False
#    return USUARIOS.get(login) == senha #return true

@auth.verify_password 
def verificacao(login, senha):
    if not(login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first() #.first() retorna o objeto no .qyer.filter_by()
class Pessoa(Resource):
    @auth.login_required
    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try: 
            response = {
                'nome':pessoa.nome, 
                'idade':pessoa.idade,
                'id':pessoa.id,
                'status':pessoa.status
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }

            
        return response
    def put(self,nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        if 'id' in dados:
            pessoa.id = dados['id']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluída com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso', 'mesagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id,'nome':i.nome,'idade':i.idade} for i in pessoas]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])                       
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade 
        }    
        return response
class ListaAtividades(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response
    
    def post(self):
        dados = request.json 
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')#URN
api.add_resource(ListaPessoas, '/pessoa/')#URN
api.add_resource(ListaAtividades,'/atividades/')#URN
if __name__ == '__main__':
    app.run(debug=True)
