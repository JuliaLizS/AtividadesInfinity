import sqlite3
import random
from criar_tabelas import criar_tabelas
from conecta_banco import (cadastrar_aluno,
                           cadastrar_curso,
                           visualizar_alunos,
                           visualizar_cursos,
                           matricular_aluno,
                           visualizar_alunos_matriculados)

criar_tabelas()

print('Seja bem vindo!\n')

while True:
    print('O que deseja fazer?')
    print('1 - CADASTRAR\n2 - CONSULTAR\n3 - MATRICULAR')
    escolha = input('Digite a escolha: ')
    if escolha == '1':
        print('Você quer cadastrar um aluno ou um curso?\n')
        print('1 - Aluno\n2 - Curso')
        opcao = input('-> ')
        if opcao == '1':
            nome_aluno = input('Digite o nome do aluno: ')
            cadastrar_aluno(nome_aluno)
            print('Aluno cadastrado com sucesso!')
            break
        elif opcao == '2':
            nome_curso = input('Digite o nome do curso: ')
            cadastrar_curso(nome_curso)
            print('Curso cadastrado com sucesso!')
            break
        else:
            print('Opção Inválida!')
    elif escolha == '2':
        print('Você deseja visualizar alunos ou cursos?\n')
        print('1 - Alunos\n2 - Cursos ')
        escolha = input('-> ')
        if escolha == '1':
            print('\n-- LISTA DE ALUNOS --\n')
            visualizar_alunos()
            break
        elif escolha == '2':
            print('\n-- LISTA DE CURSOS --\n')
            visualizar_cursos()
            break
        elif escolha == '3':
            print('-- ALUNOS MATRICULADOS --')
            visualizar_alunos_matriculados()
            break
        else:
            print('OPÇÃO INVÁLIDA')
    elif escolha == '3':
        idaluno = int(input('DIGITE O ID DO ALUNO: '))
        id_curso = int(input('DIGITE O ID DO CURSO: '))
        matricular_aluno(idaluno, id_curso)

    else:
        print('* OPÇÃO INVÁLIDA *')