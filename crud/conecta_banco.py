import sqlite3
import random

db = sqlite3.connect('banco_de_dados.db')
cursor = db.cursor()


def cadastrar_aluno(nome_aluno):
    cursor.execute(f'''
        INSERT INTO alunos (idaluno, nome_aluno)
        VALUES({random.randint(100,200)},'{nome_aluno}')
''')
    db.commit()

def cadastrar_curso(nome_curso):
    cursor.execute(f'''
        INSERT INTO cursos (id_curso, nome_curso)
        VALUES({random.randint(100,200)}, '{nome_curso}')
''')
    db.commit()

def visualizar_alunos():
    resultado = cursor.execute('SELECT * FROM alunos').fetchall()
    for tupla in resultado:
        print(f'{tupla[0]} - {tupla[1]}')

def visualizar_cursos():
    resultado = cursor.execute('SELECT * FROM cursos').fetchall()
    for tupla in resultado:
        print(f'{tupla[0]} - {tupla[1]}')

def matricular_aluno(idaluno, id_curso):
    resultado_alunos = cursor.execute('SELECT idaluno FROM alunos').fetchall()
    ids = []
    for tupla in resultado_alunos:
        ids.append(tupla[0])
    if idaluno not in ids:
        print('USUARIO NÃO CADASTRADO')
        exit()
    
    resultado_cursos = cursor.execute('SELECT id_curso FROM cursos').fetchall()
    id_cursos = []
    for tupla in resultado_cursos:
        id_cursos.append(tupla[0])
    if id_curso not in id_cursos:
        print('CURSO NÃO CADASTRADO')
        exit()

    cursor.execute(f''' INSERT INTO alunos_matriculados(idaluno, id_curso) VALUES ({idaluno}, {id_curso})
    ''')
    db.commit()

def visualizar_alunos_matriculados():
    resultado = cursor.execute('''
        SELECT a.idaluno, a.nome_aluno, c.id_curso, c.nome_curso
        FROM alunos as a
        INNER JOIN alunos_matriculados as am
        ON a.idaluno = am.idaluno
        INNER JOIN cursos as c
        ON c.id_curso = am.id_curso
    ''').fetchall()
    for tupla in resultado:
        print(f'{tupla[0]} => {tupla[1]} - {tupla[2]} => {tupla[3]}')