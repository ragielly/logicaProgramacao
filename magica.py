# -*- coding: utf-8 -*-
import os
import sys

# limpa tela (funciona em Windows e Linux)
os.system('cls' if os.name == 'nt' else 'clear')

# garante que o terminal use UTF-8
sys.stdout.reconfigure(encoding='utf-8')


print('Olhe as cartas abaixo e escolha uma:')
print('----')
print(' Q♣️ K♦️ J♥️ Q♥️ J♣️ K♠️')
input()

os.system('cls')
print('A carta que voce pensou....')
input()

print()
print('Desdapareceu!')
print()
print(' J♣️ Q♦️ J♦️ Q♠️ K♥️ J♣️')
