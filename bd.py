def get_idlogin(cursor, login, senha):
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}"')
    idlogin = cursor.fetchone()

    cursor.close()

    return idlogin[0]

def get_projetos(cursor):
    cursor.execute(f'select idlistadeprojetos, nome, datainicio, datafinal from listadeprojetos')
    projetos = cursor.fetchall()
    return projetos

def exibir_atividades(cursor, idlistadeprojetos):
    cursor.execute(f'select descricao, datainicio, datafinal, representante from projetos.listadeatividades where idlistadeprojetos="{idlistadeprojetos}"')
    proj = cursor.fetchall()
    cursor.close()
    print(proj)
    return proj