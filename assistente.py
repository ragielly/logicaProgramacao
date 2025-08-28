print('Ola, eu sou sua assistente pyth. O que  quer fazer hoje?')

comando= input('Digite um comando: ')

match comando:
    case 'oi'|'ola':
        print('oi, como vai você?😃')
    case 'tchau'|'sair'|'fim':
        print(' tchau, foi bom conversar com você!👋')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? São login 😂')
    case 'clima'|'tempo':
        print('Hoje está muito friooo 🥶')
    case _:
        print('Desculpa não entendi o comando 😕')