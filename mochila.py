CAPACIDADE = 30
PESO_MAXIMO_ITEM = 20
itens = ["Espada", "Escudo", "Poção"]
pesos = [8, 10, 1]
mochila = []
pesos_mochila = []

while True:
    print("===== MOCHILA DO AVENTUREIRO =====")
    print("1 - Ver mochila")
    print("2 - Guardar item")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if len(mochila) == 0:
            print("A mochila está vazia.")
        else:
            print("Itens na mochila:")
            for i in range(len(mochila)):
                print(f"{i + 1} - {mochila[i]} ({pesos_mochila[i]} kg)")

    elif opcao == "2":
        if len(itens) == 0:
            print("Não há mais itens para guardar.")
        else:
            print("Itens disponíveis:")
            for i in range(len(itens)):
                print(f"{i} - {itens[i]} ({pesos[i]} kg)")

            escolha = input("Qual item quer guardar? ")

            if escolha.isdigit():
                indice = int(escolha)
                if 0 <= indice < len(itens):
                    peso_item = pesos[indice]
                    peso_total = sum(pesos_mochila)

                    if peso_item > PESO_MAXIMO_ITEM:
                        print("O item é demasiado pesado para a mochila.")
                    elif peso_total + peso_item > CAPACIDADE:
                        print("A mochila está cheia.")
                    else:
                        mochila.append(itens[indice])
                        pesos_mochila.append(pesos[indice])
                        itens.pop(indice)
                        pesos.pop(indice)
                        print(f"{mochila[-1]} foi guardado na mochila.")
                else:
                    print("Opção inválida.")
            else:
                print("Opção inválida.")

    elif opcao == "3":
        print("Até à próxima aventura!")
        break

    else:
        print("Opção inválida.")