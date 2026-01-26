def calculo(salario_mensal ,desp_casa, desp_fixas, desp_lazer, desp_investimento, desp_reserva):
    gastos_mensais = sum([
        desp_casa,
        desp_fixas,
        desp_lazer,
        desp_investimento,
        desp_reserva
    ])
    
    percentual_gasto = (gastos_mensais / salario_mensal) * 100
    saldo_mensal= salario_mensal - gastos_mensais

    return gastos_mensais, percentual_gasto, saldo_mensal

def pedir_valores(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Valor inválido! digite somente números positivos.")
                continue
            return valor
        except ValueError:
            print("Valor inválido! digite um número positivo.")
    

def main():
    print("== SISTEMA DE CONTROLE DE DESPESAS ==")

    while True:
        try:
            salario_mensal = float(input("Qual o seu salário mensal? "))
            if salario_mensal < 1:
                continue
            else:
                break
        except ValueError:
            continue

    print("\nDigite suas despesas mensais: ")

    desp_fixas = pedir_valores("Despesas fixas: ")
    desp_casa = pedir_valores("Despesas da casa (água, luz, internet....): ")
    desp_lazer = pedir_valores("Despesas do lazer: ")
    desp_investimento = pedir_valores("Despesas para investir: ")
    desp_reserva = pedir_valores("Despesas Reserva: ")

    gastos_mensais, percentual_gasto, saldo_mensal = calculo(
        salario_mensal,
        desp_casa,
        desp_fixas,
        desp_lazer,
        desp_investimento,
        desp_reserva)
    
    print(f"\nTotal de gastos do mês: R${gastos_mensais:.2f}")
    print(f"Percentual do salário gasto: {percentual_gasto:.0f}%")

    if percentual_gasto < 80:
        print(f"Muito bem! Sobrou dinheiro esse mês. Saldo> {saldo_mensal:.2f}")
    elif 80 <= percentual_gasto <= 100:
        print(f"Você quase atingiu o limite. Tome cuidado! Saldo > {saldo_mensal:.2f}")
    else:
        print(f"O seu gasto passou do limite. Saldo negativo! Saldo > {abs(saldo_mensal):.2f}")

main()