def verify_nome(a=1):
    '''
    ->Função que verifica nome digitado
    :param a: a=1(nome) a=2(sobrenome)
    :return: nome_verified
    '''
    itr = True
    while itr:
        # verificando se é nome ou sobrenome
        if a == 1:
            nome_verified = input('Nome: ')
        elif a == 2:
            nome_verified = input('Sobrenome: ')
        # verificação padrão
        if len(nome_verified) < 3:
            print({'msg': f'Nome "{nome_verified}" é muito curto'})
        elif not (nome_verified.isalpha()):
            print({'msg': 'Campo não aceita caracteres numéricos'})
        else:
            interruptor = False
            return nome_verified


def verify_email():
    '''
    ->Função que verifica email digitado
    :return: valor email aceitavel (email_verified)
    '''
    itr = True
    while itr:
        email_verified = input("Emais: ")
        if len(email_verified) < 1:
            print({'msg': 'Campo não informado'})
        elif '@' in email_verified:
            print({'msg': '"@gmail.com" será adicionado automaticamente'})
        else:
            itr = False
            email_verified = email_verified + '@gmail.com'
            return email_verified


def verify_senha():
    '''
    -> Verifica a senha digitada e pede confirmação
    :return: retorna apenas senha aceitável (senha_verified)
    '''
    itr = True
    while itr:
        senha_verified = input("Senha: ")
        if len(senha_verified) < 8:
            print({'msg': 'Campo deve ter no minímo 8 caracteres'})
        elif senha_verified.isalpha() or senha_verified.isnumeric():
            print({'msg': 'Senha deve possuir números e letras'})
        else:
            itr = False
    #confirmação de senha
    while not itr:
        confirmar_senha = input('Confirmar senha: ')
        if confirmar_senha != senha_verified:
            print({'msg': 'Senhas diferentes'})
        else:
            itr = True
            return senha_verified

# TODO: crie uma função e peça, nome, sobrenome, email e senha
# rests programas qe retorna dados no estilo json


def set_usuarios(bd={}):  # save, register
    '''
    ->Função que adiciona dados de cadastro a um banco(dicionário)
    :param bd: banco(dicionário)
    :return: banco com dados cadastrados (database)
    '''
    database = bd
    primeiro_nome = verify_nome(a=1)
    sobrenome = verify_nome(a=2)
    email = verify_email()
    senha = verify_senha()


    database['nome'] = primeiro_nome
    database['sobrenome'] = sobrenome
    database['email'] = email
    database['senha'] = senha

    return database
# Banco de dados stateless, ou seja, que perde sua memória


banco_de_dados = dict()
set_usuarios(banco_de_dados)
print(banco_de_dados)
