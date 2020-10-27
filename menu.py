def menuPrincipal():
    print('-------MENU PRINCIPAL--------')
    print('1 - Paciente')
    print('2 - Médico')
    print('3 - Clinica')
    print('4 - Funcionario')
    print('0 - SAIR')
    print()

def menuPaciente():
    print('------MENU PACIENTE---------')
    print('1 - Cadastrar')
    print('2 - Buscar por CPF')
    print('3 - Listar Todos')
    print('4 - Buscar por Nome')
    print('0 - SAIR')
    print()


def menuMedico():
    print('------MENU MÉDICO---------')
    print('1 - Cadastrar')
    print('2 - Buscar por CRM')
    print('3 - Listar Todos')
    print('4 - Buscar Por Nome')
    print('5 - Buscar Por Especialização')#Existe mais de uma médico com a mesma especialização
    print('0 - SAIR')
    print()

def menuClinica():
    print('------MENU CLÍNICA---------')
    print('1 - Cadastrar')
    print('2 - Buscar por Código')#retorna somente 1
    print('3 - Buscar por cep')#Pode retornar mais de um (ListaTemp)
    print('4 - Buscar Por Sigla')#Pode retornar mais de uma
    print('5 - Listar Todos')
    print('0 - SAIR')
    print()


def menuFuncionario():
    print('------MENU Funcionario---------')
    print('1 - Cadastrar')
    print('2 - Buscar por CPF')
    print('3 - Listar Todos')
    print('4 - Buscar por Nome')
    print('5 - Buscar por CARGO') # Perguntar qual cargo deverá buscar
    print('0 - SAIR')
    print()