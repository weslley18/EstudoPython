from menu import menuMedico
from BD import todosmedicos, salvarmedico

def cadastrarmedico():
    crm = input('DIGITE O CRM: ')
    nome = input('DIGITE O NOME: ')
    contato = input('DIGITE O CONTATO: ')
    especializacao = input('digite a especializacao')
    medico = [crm, nome, contato, especializacao]
    if salvarmedico(medico) == True:
        print("medico salvo com sucesso!!!")
    else:
        print("medico ja existe")

def listarTodos():
    lista = todosmedicos()
    if len(lista) == 0:
        print('Não existe Pacientes cadastrado no Sistema')
    else:
        for i, med in enumerate(lista):
            i+=1
            print(f'medico {i}')
            print(f'crm: {med[0]}')
            print(f'NOME: {med[1]}')
            print(f'CONTATO: {med[2]}')
            print(f'especializacao: {med[3]}')

def buscarcrm(crm):
    lista = todosmedicos()
    for medico in lista:
        if medico[0]==crm:
            print(f'crm: {medico[0]}')
            print(f'NOME: {medico[1]}')
            print(f'CONTATO: {medico[2]}')
            print(f'especializacao: {medico[3]}')
            return
    print("cmr não Encontrado ")

def buscarPorNome():
    nome = input("DIGITE O NOME")
    listaTemp = []
    lista = todosmedicos()
    for medico in lista:
        if medico[1].__contains__(nome):
            listaTemp.append(medico)

    if len(listaTemp) == 0:
        print('Não existe medico com esse nome')
    else:
        for i, med in enumerate(listaTemp):
            i+=1
            print(f'PACIENTE {i}')
            print(f'CPF: {med[0]}')
            print(f'NOME: {med[1]}')
            print(f'CONTATO: {med[2]}')
            print(f'especializacao: {med[3]}')
            print('--------------')

def buscarespecializacao():
    especializacao = input("DIGITE a especialização")
    listaTemp = []
    lista = todosmedicos()
    for medico in lista:
        if medico[3].__contains__(especializacao):
            listaTemp.append(medico)

    if len(listaTemp) == 0:
        print('Não existe medico com essa especialização')
    else:
        for i, med in enumerate(listaTemp):
            i+=1
            print(f'PACIENTE {i}')
            print(f'CPF: {med[0]}')
            print(f'NOME: {med[1]}')
            print(f'CONTATO: {med[2]}')
            print(f'especializacao: {med[3]}')
            print('--------------')

def iniciarSistemamedico():
    while True:
        menuMedico()
        op = input("Digite a OPÇÃO: ")
        if op == '0':
            print('SAINDO DO medico')
            return
        if op == '1':
            cadastrarmedico()
        if op == '2':
            crm = input("DIGITE O crm")
            buscarcrm(crm)
        if op == '3':
            listarTodos()
        elif op == '4':
            buscarPorNome()
        elif op == '5':
            buscarespecializacao()
        else:
            print('Opção inválida - tente novamente!!')