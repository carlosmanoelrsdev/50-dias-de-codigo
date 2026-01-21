from datetime import date
print("-="*21)
print("Seja bem-vindo ao alistamento do exército!")
print("-="*21)

def calcular_dados(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    ano_do_alistamento = ano_nascimento + 18
    multa = None

    if idade > 18:
        multa = (ano_atual - ano_do_alistamento) * 6
    return idade, ano_do_alistamento, multa


def situacao_do_candidato(idade, ano_alistamento, multa):
    if idade == 18:
        print(f"\nO seu alistamento é esse ano!")
    elif idade > 18:
        print(f"\nO ano que você deveria fazer o alistamento foi {ano_alistamento}! Multa de R${multa:.2f} (R$6.00 por ano).")
    else:
        print(f"\nVocê é menor de idade! Seu alistamento será {ano_alistamento}")
    

def main():
    ano_atual = date.today().year

    while True:
        print("\nPara começarmos precisamos de alguns dados:")

        nome = str(input("Digite seu nome: "))
        print(f"É um prazer te conhecer {nome}!")

        while True:
            try:
                ano_nascimento = int(input("Digite seu ano de nascimento: "))
                if 1900 < ano_nascimento < ano_atual:
                    break
                else:
                    print("Ano inválido, tente novamente.\n")
                    continue
            except ValueError:
                print("Valor inválido! Digite apenas números.\n")

        idade, ano_alistamento, multa = calcular_dados(ano_nascimento)
        situacao_do_candidato(idade, ano_alistamento, multa)

        while True:
            try:
                escolha = int(input("\nDeseja continuar? [1]Sim [2]Não: "))
                if escolha == 1 or escolha == 2:
                    break
                else:
                    print("Valor inválido! Digite [1] Para SIM [2] Para NÃO.")
            except ValueError:
                print("Valor inválido! Digite [1] Para SIM [2] Para NÃO.")


        if escolha == 1:
            continue
        else:
            print("Encerrando Programa....")
            break


main()


