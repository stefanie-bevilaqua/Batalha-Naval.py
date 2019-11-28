
#------------Gera o tabuleiro------------------
def gera_tabuleiro():

    tab = [['\u2B1C'] * 20]
    for a in range(19):
        tab += [['\u2B1C'] * 20]
    return tab

#--------------Junta o tabuleiro em uma string---------
def imprime_tabuleiro(tab):#Junta as listas para ficar bonito
    col = 0
    for line in tab:
        if col > 9:
            print('  '+str(col) + ''.join(line))
        else:
            print('  0'+ str(col) + ''.join(line))
        col += 1
    print()
#-----------Escolhe o nome do Player----------
def nome_jogador():
    jogador = input('Digite o nome do jogador: ')
    return jogador

#-----------Escolhe o par onde será feita a jogada--------------
def escolhe_bloco_user(tab:list):
    while True:
        try:
            enter = input('Dados no formato x,y: ').split(',')
            linha = int(enter[0])
            coluna = int(enter[1])
        except:
            continue
        else:
            break
    return linha,coluna

#----------------Quebra o input do usuário para os navios-----------
def desmonta(entrada:str):
    primeira_parte = entrada.split(':')
    segunda_parte = primeira_parte[0].split(',')
    linha = int(segunda_parte[0])
    coluna = int(segunda_parte[1])
    direcao = primeira_parte[1]
    return linha, coluna, direcao

#----------------------Pega o input do usuário para o navio-----------------
def navio(): 
    try:
        string_inicial = input('Digite a posição inicial e direção no formato x,x:D\n ')
        return string_inicial
    except:
        pass

#---------------Verifica se acertou algum dos navios---------------------------
def acertou(log:list,linha:int,coluna:int):
    if (linha,coluna) in log:
        return True
    elif (linha,coluna) not in log:
        return False

#----------Coloca no tabuleiro o navio---------------------------
def coloca_navio_tabuleiro(tabuleiro:list,linha:int, coluna:int, direcao:str, tamanho:int,log:list):
    for bloco in range(tamanho):
        if direcao == 'N':
            if linha >= 0 and linha <= tamanho:
                continue
            else:
                if [linha,coluna] in log:
                    linha -= 1
                else:
                    log.append((linha,coluna))
                    tabuleiro[linha][coluna] = '\u2B1B'
                    linha -= 1
        elif direcao == 'S':
            if linha <=19 and linha >= tamanho:
                continue
            else:
                if [linha,coluna] in log:
                    linha += 1
                else:
                    log.append((linha,coluna))
                    tabuleiro[linha][coluna] = '\u2B1B'
                    linha += 1
        elif direcao == 'L':
            if coluna <= 19 and coluna >= tamanho:
                continue
            else:
                if [linha,coluna] in log:
                    coluna += 1
                else:
                    log.append((linha,coluna))
                    tabuleiro[linha][coluna] = '\u2B1B'
                    coluna += 1
        elif direcao == 'O':
            if coluna >= 0 and coluna <=tamanho:
                continue
            else:
                if [linha,coluna] in log:
                    coluna -= 1
                else:
                    log.append((linha,coluna))
                    tabuleiro[linha][coluna] = '\u2B1B'
                    coluna -= 1
    return tabuleiro, log

#--------------Pega os navios do computador--------------------
def coloca_navio_computador_tabuleiro(tabuleiro:list,tamanho:int,direcoes:list,log:list):
    import random
    linha = random.randint(0,20)
    coluna = random.randint(0,20)
    direcao = random.choice(direcoes)
    for bloco in range(tamanho):
            if direcao == 'N':
                tabuleiro[linha][coluna] = '\u2B1C'
                log.append((linha,coluna))
                linha -= 1
            elif direcao == 'S':
                tabuleiro[linha][coluna] = '\u2B1C'
                log.append((linha,coluna))
                linha += 1
            elif direcao == 'L':
                tabuleiro[linha][coluna] = '\u2B1C'
                log.append((linha,coluna))
                coluna += 1
            elif direcao == 'O':
                tabuleiro[linha][coluna] = '\u2B1C'
                log.append((linha,coluna))
                coluna -= 1
    return tabuleiro, log

#-----------------Computador escolhe onde vai tentar acertar------------------
def escolhe_bloco_computador():
    import random
    linha = random.randint(0,19)
    coluna = random.randint(0,19)
    return linha,coluna

#-------------------Mostra os tabuleiros------------------------
def mostra_tabs(tabuleiro_usuario:list, tabuleiro_computador:list):
    print('-=-'*5+'Tabuleiro do usuário'+'-=-'*5)
    imprime_tabuleiro(tabuleiro_usuario)
    print('-=-'*5+'Tabuleiro do computador'+'-=-'*5)
    imprime_tabuleiro(tabuleiro_computador)

#-------------Retira um elemento do log dos navios---------------------
def remove_pedaco(item:tuple,log:list):
    if item in log:
        index = log.index(item)
        log.pop(index)
    return log

#----------------Verifica se o jogo acabou-----------------------------
def acaba_jogo(log:list):
    if len(log) > 0:
        return True
    return False

#--------------Escolhe a dificuldade do jogo----------------------
def dificuldade():
    while True:
        try:
            dif = int(input('1 para normal e 2 para impossível: '))
            if dif != 1 and dif != 2:
                continue
            return  dif
        except:
            print('Digite um valor válido')
            continue

#---------------Jogada computador modo difícil--------------------------
def jogada_hard(log:list):
    while True:
        try:
            index = 0
            linha, coluna = log.pop(index)
            return linha, coluna
        except:
            continue

#----------------------------------------------FUNÇÕES DECORATIVAS----------------------------------------------
#-------------Mapeamento---------------
def mapeia():
    import time
    print()
    print('Mapeando área do jogo.')
    time.sleep(0.5)
    print('Mapeando área do jogo..')
    time.sleep(0.5)
    print('Mapeando área do jogo...')
    time.sleep(0.5)
    print('Mapeando área do jogo....')
    time.sleep(0.5)
    print('Feito!!')
    time.sleep(1)
    print()