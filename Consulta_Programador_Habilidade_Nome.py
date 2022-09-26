from Programador_Habilidade_tabela_ import Programadores,Habilidades

def insere_programadores():
    programador = Programadores(nome='Julia', idade=19)
    print(programador)
    programador.save()
def consulta_programador():
    programadores = Programadores.query.all()
    print(programadores)
def insere_habilidades():
    habilidade = Habilidades(nome='ux desing')
    print(habilidade)
    habilidade.save()
def consulta_habilidades():
    habilidades = Habilidades.query.all()
    print(habilidades) 
if __name__ == '__main__':
    insere_programadores()
    insere_habilidades()
    consulta_programador()
    consulta_habilidades()