class Elevador:
    #atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar,
    def __init__(self, totalCapacidade, totalAndares):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndares = totalAndares
        self.atualAndar = 0
    
    # metodos: subir, descer, entrar, sair
    def subir(self):
        if self.atualAndar >= self.totalAndares - 1:
            print('Você está no andar mais alto!')
        else:
            self.atualAndar += 1
            print(f'Subindo! Andar atual: {self.atualAndar}')
    
    def descer(self):
        if self.atualAndar <= 0:
            print('Você está no térreo!')
        else:
            self.atualAndar -= 1
            print(f'Descendo! Andar atual: {self.atualAndar}')
    
    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print(f'Entrando uma pessoa! Capacidade atual: {self.atualCapacidade}')
        else:
            print('O elevador está cheio!')
    
    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print(f'Saindo uma pessoa! Capacidade atual: {self.atualCapacidade}')
        else:
            print('Não tem ninguém no elevador!')


# Função pra escolher o andar 
def escolher_andar(elevador, andarDesejado):
    if andarDesejado < 0 or andarDesejado >= elevador.totalAndares:
        print("Andar inválido.")
        return

    while elevador.atualAndar < andarDesejado:
        elevador.subir()
    while elevador.atualAndar > andarDesejado:
        elevador.descer()
    print(f"Você chegou ao andar {elevador.atualAndar}.")

# Quantidades do elevador
elevador = Elevador(totalCapacidade=10, totalAndares=20)

# Menu
while True:
    print("\n***** Opções: *****\n1. Escolher andar\n2. Entrar\n3. Sair\n4. Sair do programa")
    
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        andarDesejado = int(input("Digite o andar desejado: "))
        escolher_andar(elevador, andarDesejado)
    elif escolha == '2':
        elevador.entrar()
    elif escolha == '3':
        elevador.sair()
    elif escolha == '4':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
