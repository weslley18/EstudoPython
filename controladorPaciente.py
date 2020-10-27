from menu import menuPaciente
from BD import salvarPaciente, todosPacientes


def cadastrarPaciente():
    cpf = input('DIGITE O CPF: ')
    nome = input('DIGITE O NOME: ')
    contato = input('DIGITE O CONTATO: ')
    paciente = [cpf, nome, contato]
    if salvarPaciente(paciente) == True:
        print("PACIENTE SALVO COM SUCESSO!!!")
    else:
        print("PACIENTE JÁ EXISTE")


def listarTodos():
    lista = todosPacientes()
    if len(lista) == 0:
        print('Não existe Pacientes cadastrado no Sistema')
    else:
        for i, pac in enumerate(lista):
            i+=1
            print(f'PACIENTE {i}')
            print(f'CPF: {pac[0]}')
            print(f'NOME: {pac[1]}')
            print(f'CONTATO: {pac[2]}')
            print('--------------')
def buscarcpf(cpf):
    lista = todosPacientes()
    for  paciente in lista:
        if paciente[0]==cpf:
            print(f'CPF: {paciente[0]}')
            print(f'NOME: {paciente[1]}')
            print(f'CONTATO: {paciente[2]}')
            print('--------------')
            return
    print("CPF não Encontrado ")

def buscarPorNome():
    nome = input("DIGITE O NOME")
    listaTemp = []
    lista = todosPacientes()
    for paciente in lista:
        if paciente[1].__contains__(nome):
            listaTemp.append(paciente)

    if len(listaTemp) == 0:
        print('Não existe Pacientes com esse nome')
    else:
        for i, pac in enumerate(listaTemp):
            i+=1
            print(f'PACIENTE {i}')
            print(f'CPF: {pac[0]}')
            print(f'NOME: {pac[1]}')
            print(f'CONTATO: {pac[2]}')
            print('--------------')

def iniciarSistemaPaciente():
    while True:
        menuPaciente()
        op = input("Digite a OPÇÃO: ")
        if op == '0':
            print('SAINDO DO PACIENTE')
            return
        if op == '1':
            cadastrarPaciente()
        elif op == '2':
            cpf = input("DIGITE O CPF")
            buscarcpf(cpf)
        elif op == '3':
            listarTodos()
        else:
            print('Opção inválida - tente novamente!!')
