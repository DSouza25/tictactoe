from os import system
from time import sleep
from random import randint
turno = 'O'
# mostrar o tabuleiro no console;
def mostrarJogo():
    system('cls')
    print('''=================
  Jogo da velha
=================''')
    print(f'    Vez do {turno}')
    print('-----------------')
    for n, celula in enumerate(tabuleiro):
        if (n+1) % 3 == 0:
            print(celula, end='\n')
            if (n+1) != 9:
                print('----------')
        else:
            print(celula, end=' | ')
# Executando a jogada da vez
def jogadaTurno():
    while True:
        if turno == 'X' and bot:
            jogada = randint(0, 8)
            sleep(1)
        else:
            jogada = int(input('Em qual posição, de 0 a 8, você deseja jogar? '))
        if 0 <= jogada <= 8:
            if celulas[jogada] not in 'XO':
                celulas.insert(jogada, turno)
                tabuleiro.insert(jogada, turno)
                del celulas[jogada + 1]
                del tabuleiro[jogada + 1]
                break
            else:
                if turno == 'O' or bot == False:
                    print('Jogada inválida! Este lugar já foi marcado.')
                    sleep(1)
        else:
            print('Jogada inválida')
            sleep(1)
# Trocando a vez do jogador
def mudarTurno(turno):
    if turno in 'X':
        turno = 'O'
    else:
        turno = 'X'
    return turno

# Verificando as condições de vitória
def testeVencedor(jogo, jogador):
    empate = False
    vazio = False
    temVencedor = False
    vencedor = 'nenhum'
    if jogo[0] == jogo[1] == jogo[2]:
        temVencedor = True
    elif jogo[0] == jogo[4] == jogo[8]:
        temVencedor = True
    elif jogo[0] == jogo[3] == jogo[6]:
        temVencedor = True
    elif jogo[3] == jogo[4] == jogo[5]:
        temVencedor = True
    elif jogo[6] == jogo[7] == jogo[8]:
        temVencedor = True
    elif jogo[6] == jogo[4] == jogo[2]:
        temVencedor = True
    elif jogo[1] == jogo[4] == jogo[7]:
        temVencedor = True
    elif jogo[2] == jogo[5] == jogo[8]:
        temVencedor = True
    for celula in jogo:
        if celula not in 'XO':
            vazio = True
    if vazio == False and temVencedor == False:
        empate = True
    if temVencedor:
        return {'vencedor': f'   Vitória do {jogador}',
                'acabou': True}
    else:
        if empate:
            return {'vencedor': 'Empatou!',
                    'acabou': True}
        else:
            return {'acabou': False}

# ----- Programa -----
while True:
    print('='*30)
    print(f'{"Jogo da Velha":^30}')
    print('='*30)
    celulas = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    solo = str(input('Você quer jogar contra IA? [S/N] ')).strip()
    bot = False
    if solo[0] in 'Ss':
        bot = True
        print('Ok, você começa.')
        sleep(1)
    input('Pressione ENTER para começar...')
    while True:
        mostrarJogo()
        jogadaTurno()
        vencedor = testeVencedor(celulas, turno)
        print(vencedor)
        if vencedor['acabou']:
            break
        turno = mudarTurno(turno)

    system('cls')
    print('='*20)
    print(f'{vencedor["vencedor"]:^20}')
    print('='*20)
    resp = str(input('Deseja recomeçar? [S/N] ')).strip()
    if resp[0] in 'Nn':
        break
    system('cls')