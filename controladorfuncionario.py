from menu import menuFuncionario
from BD import salvarfuncionario, todosfuncionarios

def cadastrarfuncionario():
    cpf = int(input('digite o cpf: '))
    nome = input('informe o nome do funcionario: ')
    cargo = input('informe o cargo: ')
    salario = int(input('informe o salario: '))
    funcionarios = [cpf, nome, cargo, salario]
    if salvarfuncionario(funcionarios) == True:
        print('funcionario salvo com sucesso')
    else:
        print('funcionario ja existe')

def buscarcpf(cpf):
    lista = todosfuncionarios()
    for funcionarios in lista:
        if funcionarios[0] == cpf:
            print(f'cpf: {funcionarios[0]}')
            print(f'nome: {funcionarios[1]}')
            print(f'cargo: {funcionarios[2]}')
            print(f'salario: {funcionarios[3]}')
            return
        else:
            print('cpf nao encontrando')
def listartodos():
    lista = todosfuncionarios()
    if len(lista) == 0:
        print('nao existe funcionario cadastrado')
    else:
        for i, fun in enumerate(lista):
            i = i+1
            print(f'funcionario{i}')
            print(f'cpf: {fun[0]}')
            print(f'nome: {fun[1]}')
            print(f'cargo:{fun[2]}')
            print(f'salario: {fun[3]}')
def buscarnome():
    nome = input('informe o nome: ')
    listatemp = []
    lista = todosfuncionarios()
    for funcionarios in lista:
        if funcionarios[1].__contains__(nome):
            listatemp.append(funcionarios)
    if len(listatemp) == 0:
        print('nao existe funcionario com esse nome')
    else:
        for i, fun in enumerate(listatemp):
            i += 1
            print(f'funcionario{i}')
            print(f'cpf: {fun[0]}')
            print(f'nome: {fun[1]}')
            print(f'cargo: {fun[2]}')
            print(f'salario: {fun[3]}')

def buscarcargo():
    cargo = input('informe o cargo')
    listatemp = []
    lista = todosfuncionarios()
    for funcionarios in lista:
        if funcionarios[2].__contains__(cargo):
            listatemp.append(funcionarios)
    if len(listatemp) == 0:
        print('nao existe esse cargo')
    else:
        for i, fun in enumerate(listatemp):
            i += 1
            print(f'funcionario{i}')
            print(f'cpf: {fun[0]}')
            print(f'nome: {fun[1]}')
            print(f'cargo: {fun[2]}')
            print(f'salario: {fun[3]}')
def iniciarsistemafuncionario():
    while True:
        menuFuncionario()
        op = input('digite a opção')
        if op == '0':
            print('saindo do funcionario')
            return
        if op == '1':
            cadastrarfuncionario()
        if op == '2':
            cpf = int(input('informe o cpf'))
            buscarcpf(cpf)
        if op == '3':
            listartodos()
        if op == '4':
            buscarnome()
        elif op == '5':
            buscarcargo()
        else:
            print('opção invalida - tente novamente')