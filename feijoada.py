#  Váriaveis
op_feijoada_escolhida = 0
va_total_acomp = 0
vo_feijoada_escolhida = 0
va_op_feijoada_escolhida = 0

#  Idendificação do produto/loja
print('Olá, Seja bem-vindo à feijoada Vergara do Chefe Murilo Vergara :)')

#  Função def para o volume da feijoada conforme pedido no exercicio
def volumeFeijoada():

    # variaveis de uso global
    global vo_feijoada_escolhida
    global op_acomp
    global va_acomp

    # Loop do volume da feijoada desejada.
    while (True):
        print('Volume que deseja comprar!')
        #  Msg de erro cada digite uma str
        try:
            vo_feijoada_escolhida = int(input('Qual a quantidade que o Sr(a) deseja comprar em (ml): '))
            if (vo_feijoada_escolhida >= 300 and vo_feijoada_escolhida <=5000):
                opcaoFeijoada()
                break
            else:
                print('Aceitamos apenas porções maiores que 300ml ou menores que 5l! Insira um valor correto!')
                continue
        except:
            print('Por favor insira um número!')
            continue

def opcaoFeijoada():

    # variaveis de uso global novamente
    global op_feijoada_escolhida
    global va_op_feijoada_escolhida

    while (True):

        # Mensagens de Menu da feijoada
        print('Cardapio de Feijoadas')
        print('Escolha sua Feijoada: ')

        print('b - Básica (Feijão + paiol + costelinha) ')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')

        op_feijoada_escolhida = input('>>')

        #  verificando opção
        if (op_feijoada_escolhida == 'b'):
            # Atribui o valor da opção escolhida
            va_op_feijoada_escolhida = 1
            # Chama a função acompanhamento
            acompFeijoada()
            # Para o loop
            break
        elif (op_feijoada_escolhida == 'p'):
            # Atribui o valor da opção escolhida
            va_op_feijoada_escolhida = 1.25
            # Chama a função acompanhamento
            acompFeijoada()
            # Para o loop
            break
        elif (op_feijoada_escolhida == 's'):
            # Atribui o valor da opção escolhida
            va_op_feijoada_escolhida = 1.50
            # Chama a função acompanhamento
            acompFeijoada()
            # Para o loop
            break
        else:
            # Não seja obdecida nenhuma condição acima, mostra que a entrada foi ínválida.
            print('Valor inválido :( . Insira um valor valido!')
            # Continua o loop
            continue

def acompFeijoada():
    # variavel global
    global va_total_acomp

    while (True):
        # acompanhamentos

        print('Deseja algo mais ?')
        print('0- Não desejo mais acompanhamentos (encerrar pedido)')
        print('1- 200g de arroz')
        print('2- 150g de farofa especial')
        print('3- 100g de couve cozida')
        print('4- 1 laranja descascada')

        # entrada do acompanhamento
        op_acomp = input('>>')
        if (op_acomp == '0'):

            # Cálculo do volume
            volume = 0.08 * vo_feijoada_escolhida

            # Calculo do total a pagar
            valor_cobrado = volume * va_op_feijoada_escolhida + va_total_acomp
            # Valor total a ser pago!
            print('O valor cobrado é de (R$): {:.2f}'.format(valor_cobrado, volume, va_op_feijoada_escolhida, va_total_acomp))

            # Para o loop
            break
        elif (op_acomp == '1'):
            # Acrescenta o valor do novo acompanhamento ao valor total de todos os acompanhamentos até então escolhidos.
            va_total_acomp += 5
            # Cotinua o loop
            continue
        elif (op_acomp == '2'):
            # Acrescenta o valor do novo acompanhamento ao valor total de todos os acompanhamentos até então escolhidos.
            va_total_acomp += 6
            continue
        elif (op_acomp == '3'):
            # Acrescenta o valor do novo acompanhamento ao valor total de todos os acompanhamentos até então escolhidos.
            va_total_acomp += 7
            # Cotinua o loop
            continue
        elif (op_acomp == '4'):
            # Acrescenta o valor do novo acompanhamento ao valor total de todos os acompanhamentos até então escolhidos.
            va_total_acomp += 3
            # Cotinua o loop
            continue
        else:
            # Cotinua o loop
            continue

volumeFeijoada()
