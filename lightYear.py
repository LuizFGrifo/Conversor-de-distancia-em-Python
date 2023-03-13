def float_input(prompt):
    while True:
        try:
            value = float(input(prompt).replace(',', ''))
            return value
        except ValueError:
            print("Entrada inválida. Digite um número válido")


# função para converter anos luz em km
def anoLuzKm():
    lightYear = input('\nDigite quantos anos luz, você deseja converter para Km: ')
    # Converte anos luz em km usando a fórmula: 1 ano luz = 9,461e+12 km
    km = float(lightYear) * 9.461e+12
    print(f'\n{lightYear} ano luz, equivale a {km:,.3f} Km\n')


# função para converter km em anos luz
def kmAnoLuz():
    km = input('\nDigite os km, que você deseja converter para anos luz: ')
    km = km.replace(',', '') # Remove as virgulas
    # Converte km em anos luz usando a fórmula: 1 km = 9,461e-13 anos luz
    lightYear = float(km) * 9.461e-13
    print(f'\n{km} Km equivale a {lightYear}ly\n')


print('********* Bem vindo ao conversor de unidade de comprimento !!! *********\n')

while True:

    escolha = input('0 - sair\n1 - converter anos luz para km\n2 - converter km para anos luz\n: ')

    if escolha == '1':
        anoLuzKm()
        break
    elif escolha == '2':
        kmAnoLuz()
        break
    elif escolha == '0':
        print('saindo...')
        break
    else:
        print('Opção invalida !!!')

