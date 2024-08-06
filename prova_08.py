



lista_compras = []

totalProdutos = 0

def adicionar_produto():
    global totalProdutos
    try:
        produto = input("Nome do produto: ").strip()
        if not produto:
            print("Nome do produto não pode ser vazio.")
            return
        
        valor = float(input("Valor unitário do produto: ").strip())
        if valor <= 0:
            print("Valor unitário deve ser maior que zero.")
            return
        
        quantidade = int(input("Quantidade do produto: ").strip())
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return
        
        total = valor * quantidade
        lista_compras.append({
            "produto": produto,
            "valor": valor,
            "quantidade": quantidade,
            "total": total
        })
        totalProdutos += total
        print(f"{produto} adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def ver_lista():
    if not lista_compras:
        print("A lista de compras está vazia.")
    else:
        print("\nLista de Compras:")
        for item in lista_compras:
            print(f"Produto: {item['produto']}, Valor Unitário: {item['valor']:.2f}, Quantidade: {item['quantidade']}, Total: {item['total']:.2f}")
        print(f"\nValor total de todos os produtos: {totalProdutos:.2f}")

def atualizar_produto():
    global totalProdutos
    produto_atualizar = input("Nome do produto a ser atualizado: ").strip()
    for item in lista_compras:
        if item["produto"] == produto_atualizar:
            try:
                totalProdutos -= item["total"]
                novo_produto = input("Novo nome do produto (pressione Enter para manter o mesmo): ").strip() or item["produto"]
                
                novo_valor = input(f"Novo valor unitário do produto (atual: {item['valor']}): ").strip()
                novo_valor = float(novo_valor) if novo_valor else item["valor"]
                
                nova_quantidade = input(f"Nova quantidade do produto (atual: {item['quantidade']}): ").strip()
                nova_quantidade = int(nova_quantidade) if nova_quantidade else item["quantidade"]
                
                novo_total = novo_valor * nova_quantidade
                item.update({
                    "produto": novo_produto,
                    "valor": novo_valor,
                    "quantidade": nova_quantidade,
                    "total": novo_total
                })
                totalProdutos += novo_total
                print(f"{produto_atualizar} atualizado com sucesso!")
                return
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                totalProdutos += item["total"]  # Restaurar o total anterior se a atualização falhar
                return
    print("Produto não encontrado.")

def remover_produto():
    global totalProdutos
    produto_remover = input("Nome do produto a ser removido: ").strip()
    for item in lista_compras:
        if item["produto"] == produto_remover:
            totalProdutos -= item["total"]
            lista_compras.remove(item)
            print(f"{produto_remover} removido com sucesso!")
            return
    print("Produto não encontrado.")

def encerrar_programa():
    print("Encerrando o programa...")
    exit()

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            ver_lista()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            encerrar_programa()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
