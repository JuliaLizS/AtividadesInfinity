'''
Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
'''

notas = []



def inserir_notas():
    while True:
        resp = input('Deseja inserir uma nota? [S/N]')
        if resp in 'Ss':
            notas.append(float(input("Insira a nota: ")))
        elif resp in 'Nn':
            print(f'Suas notas: {notas}')
            break
        else:
            print(f'Você digitou um caractere diferente')

def calcular_media():
    if not notas:
        print('Você ainda não inseriu suas notas.')
    else:
        media = sum(notas)/len(notas)
        print(f'Sua media é: {media}')
        return media


def verificar_situacao(media):
    if media is None:
        print('Calcule a media antes de verificar a situação')
    elif media < 7:
        print('Aluno reprovado!')
    elif media == 10:
        print('Parabéns! Sua média é 10!')
    else:
        print('Você foi aprovado!')

while True:
    print('(A) para inserir as notas')
    print('(B) para calcular a média')
    print('(C) para verificar a situação')
    print('(S) para Sair')

    op = input('Digite a opção desejada: ')

    if op in 'Aa':
        inserir_notas()
    elif op in 'Bb':
        media = calcular_media()
    elif op in 'Cc':
        if 'media' not in locals():
            print('Calcule sua media antes')
        else:
            verificar_situacao(media)
    elif op in 'Ss':
        break
    else:
        print('Você digitou uma opção inexistente')