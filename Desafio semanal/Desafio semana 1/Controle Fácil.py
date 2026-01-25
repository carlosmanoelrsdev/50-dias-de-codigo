def calculo_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    maior_venda = max(vendas)
    menor_venda = min(vendas)

    return total_vendas, media_vendas, maior_venda, menor_venda

def main():
    vendas = []

    print("Bem-Vindo ao Controle Fácil.\n" \
    "Vamos ajudar no seu controle de vendas!")

    while True:
        try:
            quant_de_vendas = int(input("\nQuantas vendas foram realizadas? "))
            if quant_de_vendas < 1:
                print("Digite um número maior que 0")
                continue
        except ValueError:
            print("Valor inválido! Digite somente números!")
            continue

        for c in range(1, quant_de_vendas+1):
            while True:
                try:
                    vendas_temp = float(input(f"Digite a sua {c} venda: ").replace(",", "."))
                    if vendas_temp < 1:
                        continue
                    else: 
                        break
                except ValueError:
                    print("Valor inválido! Digite somente números.")

            vendas.append(vendas_temp)

        total, media, maior, menor = calculo_vendas(vendas)
        break

    print("\nResumo do seu dia:\n" \
    f"Total de vendas: {quant_de_vendas}\n" \
    f"Valor do Total vendido: R$ {total:.2f}\n" \
    f"Média por venda: R$ {media:.2f}\n" \
    f"Maior venda: R${maior:.2f}\n" \
    f"Menor venda: R${menor:.2f}\n")

main()