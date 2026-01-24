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

    quant_de_vendas = int(input("\nQuantas vendas foram realizadas? "))
    for c in range(1, quant_de_vendas+1):
        vendas_temp = float(input(f"Digite a sua {c} venda: "))
        vendas.append(vendas_temp)
    
    total, media, maior, menor = calculo_vendas(vendas)

    print("\nResumo do seu dia:\n" \
    f"Total de vendas: {quant_de_vendas}\n" \
    f"Valor do Total vendido: R$ {total}\n" \
    f"Média por venda: R$ {media}\n" \
    f"Maior venda: R${maior}\n" \
    f"Menor venda: R${menor}\n")

main()
