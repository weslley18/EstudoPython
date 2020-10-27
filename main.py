from menu import menuPrincipal
from controladorPaciente import iniciarSistemaPaciente
from controladormedico import iniciarSistemamedico
from controladorclinica import iniciarsistemaclinica
from controladorfuncionario import iniciarsistemafuncionario


def iniciarSistema():
    while True:
        menuPrincipal()
        op = input("Digite a OPÇÃO: ")
        if op == '0':
            print('SAINDO DO SISTEMA')
            return
        if op == '1':
            iniciarSistemaPaciente()
        if op == '2':
            iniciarSistemamedico()
        if op == '3':
            iniciarsistemaclinica()
        elif op == '4':
            iniciarsistemafuncionario()
        else:
            print('Opção inválida - tente novamente!!')


iniciarSistema()
