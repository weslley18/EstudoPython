#paciente = [cpf, nome, contato]
    # - NÃO PODE EXISTE MAIS DE UM PACIENETE COM O MESMO CPF
_pacientes = []
# medico = [CRM, nome, contato, especializacao]
    #- NÃO PODE EXISTE UM MÉDICO COM O MESMO CRM
_medicos = []
# clinica = [Codigo, nome, sigla, cep]
    #- NÃO PODE EXISTE MAIS DE UMA CLINICA COM O MESMO CÓDIGO
_clinicas = []
# funcionario = [cpf, nome, cargo, salario]
    # - NÃO PODE EXISTE MAIS DE UM FUNCIONARIO COM O MESMO CPF
    #-cargo (ATENDENTE / LIMPEZA)
_funcionarios = []

_consultas = []


def salvarPaciente(paciente):
    _pacientes.append(paciente)
    return True

def todosPacientes():
    return _pacientes.copy()

def salvarmedico(medico):
    _medicos.append(medico)
    return True

def todosmedicos():
    return _medicos.copy()

def salvarclinica(clinica):
    _clinicas.append(clinica)
    return True

def todasclinicas():
    return _clinicas.copy()

def salvarfuncionario(funcionarios):
    _funcionarios.append(funcionarios)

def todosfuncionarios():
    return _funcionarios.copy()
