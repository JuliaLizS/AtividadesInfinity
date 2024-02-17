import sqlite3

db = sqlite3.connect('banco_de_dados.db')
cursor = db.cursor()

def criar_tabelas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
            alunos (idaluno INT primary key,
                nome_aluno);
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
            cursos (id_curso INT primary key,
                    nome_curso);
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
            alunos_matriculados(idaluno INT, id_curso INT)
    ''')