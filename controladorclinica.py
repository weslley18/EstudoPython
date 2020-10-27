from menu import menuClinica
from BD import salvarclinica, todasclinicas

def cadastraclinica():
    codigo = int(input('digite o codigo da clinica: '))
    nome = input('digite o nome da clinica: ')
    sigla = input('digite a sigla da clinica: ')
    cep = int(input('informe o cep da clinica: '))
    clinica = [codigo, nome, sigla, cep]
    if salvarclinica(clinica) == True:
        print('clinica salva com sucesso')
    else:
        print('clinica ja existe')
def buscarcodigo(codigo):
    lista = todasclinicas()
    for clinica in lista:
        if clinica[0]==codigo:
            print(f'codigo: {clinica[0]}')
            print(f'nome: {clinica[1]}')
            print(f'sigla: {clinica[2]}')
            print(f'cep: {clinica[3]}')
            return
        else:
            print('codigo nao encontrado')
def buscarcep(cep):
    lista = todasclinicas()
    for clinica in lista:
        if clinica[3]==cep:
            print(f'codigo: {clinica[0]}')
            print(f'nome: {clinica[1]}')
            print(f'sigla: {clinica[2]}')
            print(f'cep: {clinica[3]}')
            return
        else:
            print('cep nao encontrado')
def buscarsigla(sigla):
    lista = todasclinicas()
    for clinica in lista:
        if clinica[2]==sigla:
            print(f'codigo: {clinica[0]}')
            print(f'nome: {clinica[1]}')
            print(f'sigla: {clinica[2]}')
            print(f'cep: {clinica[3]}')
            return
        else:
            print('sigla nao encontrada')
def listartodos():
    lista = todasclinicas()
    if len(lista) == 0:
        print('nao existe clinica cadastrada no sistema')
    else:
        for i, cli in enumerate(lista):
            i += 1
            print(f'clinica {i}')
            print(f'codigo: {cli[0]}')
            print(f'nome: {cli[1]}')
            print(f'sigla: {cli[2]}')
            print(f'cep: {cli[3]}')

def iniciarsistemaclinica():
    while True:
        menuClinica()
        op = input('digite a opção: ')
        if op == '0':
            print('saindo da clinica')
            return
        if op == '1':
            cadastraclinica()
        if op == '2':
            codigo = int(input('digite o codigo: '))
            buscarcodigo(codigo)
        if op == '3':
            cep = int(input('informe o cep: '))
            buscarcep(cep)
        elif op == '4':
            sigla = input('informe a sigla: ')
            buscarsigla(sigla)
        elif op == '5':
            listartodos()
        else:
            print('opção invalida - tente novamente')
