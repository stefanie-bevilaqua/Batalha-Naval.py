import funcoes_batalha as funcao
import time
#-----------------Decoração---------------
print('Bem-vindo ao jogo de Batalha Naval em Python 3!!')
print()
time.sleep(1.5)
print('Você primeiramente digitará seu nome e escolherá a dificuldade')
print('PS. O impossível realmente é impossível!!')
time.sleep(1.5)
print('Desejo boa sorte!!')
print()

#----------------Constantes-------------------
TAMANHOS_NAVIOS = [7,6,5,4,3]
DIRECOES_POSSIVEIS = ['N','S', 'L', 'O']
NOME_JOGADOR = funcao.nome_jogador()
DIFICULDADE = funcao.dificuldade()

#----------------------Variáveis------------------
tabuleiro_usuario = funcao.gera_tabuleiro()
tabuleiro_computador = funcao.gera_tabuleiro()
log_posicao_navios_computador = []
log_posicao_navios_user = []
jogo = True
log_posicoes_jogadas_user = []
log_posicoes_jogadas_computador = []

#-----------Mostra os tabuleiros iniciais---------------
funcao.mapeia()
funcao.mostra_tabs(tabuleiro_usuario,tabuleiro_computador)

#------Coloca os navios no tabuleiro do usuário------------
for tamanho_navio in TAMANHOS_NAVIOS:
    try:
        string_navio = funcao.navio()
        linha_inicial, coluna_inicial, direcao = funcao.desmonta(string_navio)
        tabuleiro_usuario, log_posicao_navios_user = funcao.coloca_navio_tabuleiro(tabuleiro_usuario,linha_inicial,coluna_inicial,direcao,tamanho_navio,log_posicao_navios_user)
    except IndexError:
        continue

#--------Coloca os navios do computador-----------
print('Esperando o computador colocar os navios.')
time.sleep(0.5)
print('Esperando o computador colocar os navios..')
time.sleep(0.5)
print('Esperando o computador colocar os navios...')
time.sleep(0.5)
print('Esperando o computador colocar os navios....')
time.sleep(0.5)
print('Pronto!!')
print()
for tipo_navio in TAMANHOS_NAVIOS:
    try:
        tabuleiro_computador,log_posicao_navios_computador = funcao.coloca_navio_computador_tabuleiro(tabuleiro_computador,tipo_navio,DIRECOES_POSSIVEIS,log_posicao_navios_computador)
    except IndexError:
        continue

#----------------Início do jogo-----------------
funcao.mapeia()
funcao.mostra_tabs(tabuleiro_usuario,tabuleiro_computador)
while jogo:
    #---------Começam as tentativas de acerto-------------------
    #Tentativa do user
    while True:
        linha_jogada_user, coluna_jogada_user = funcao.escolhe_bloco_user(tabuleiro_computador)
        if (linha_jogada_user,coluna_jogada_user) not in log_posicoes_jogadas_user:
            tabuleiro_computador[linha_jogada_user][coluna_jogada_user] = '\u2B1B'
            log_posicoes_jogadas_user.append((linha_jogada_user,coluna_jogada_user))
            break
        else:
            continue

    #-------------------Verifica se houve acerto do user---------------------------------
    if funcao.acertou(log_posicao_navios_computador,linha_jogada_user,coluna_jogada_user):
        print('Você afundou uma parte do navio, Parabéns!')
        tabuleiro_computador[linha_jogada_user][coluna_jogada_user] = 'XX'
        log_posicao_navios_computador = funcao.remove_pedaco((linha_jogada_user,coluna_jogada_user),log_posicao_navios_computador)
    else:
        print('Errou! Tente novamente')
    
    #Tentativa do computador
    print()
    print('Esperando o computador jogar.')
    time.sleep(0.5)
    print('Esperando o computador jogar..')
    time.sleep(0.5)
    print('Esperando o computador jogar...')
    time.sleep(0.5)
    print('Esperando o computador jogar....')
    time.sleep(0.5)
    print('Pronto!!')
    if DIFICULDADE == 1:
        while True:
            linha_jogada_computador, coluna_jogada_computador = funcao.escolhe_bloco_computador()
            if (linha_jogada_computador,coluna_jogada_computador) not in log_posicoes_jogadas_computador:
                tabuleiro_usuario[linha_jogada_computador][coluna_jogada_computador] ='\u2B1B'
                log_posicoes_jogadas_computador.append((linha_jogada_computador,coluna_jogada_computador))
                break
            else:
                continue
    else:
        while True:
            linha_jogada_computador, coluna_jogada_computador = funcao.jogada_hard(log_posicao_navios_user)
            if (linha_jogada_computador,coluna_jogada_computador) not in log_posicoes_jogadas_computador:
                tabuleiro_usuario[linha_jogada_computador][coluna_jogada_computador] = 'XX'
                log_posicoes_jogadas_computador.append((linha_jogada_computador,coluna_jogada_computador))
                break
            else:
                continue

    #--------------Verifica se houve acerto do computador---------------------------
    if funcao.acertou(log_posicao_navios_computador,linha_jogada_user,coluna_jogada_user):
        log_posicao_navios_user = funcao.remove_pedaco((linha_jogada_computador,coluna_jogada_computador),log_posicao_navios_user)
        tabuleiro_usuario[linha_jogada_computador][coluna_jogada_computador] = 'XX'

    #------------------Mostra a situação dos tabuleiros-----------------------------
    funcao.mapeia()
    funcao.mostra_tabs(tabuleiro_usuario,tabuleiro_computador)
    
    #----------------Verifica se o jogo já acabou-----------------------
    if not (funcao.acaba_jogo(log_posicao_navios_user)):
        jogo = False
        print('O computador ganhou essa, mais sorte na próxima')
    elif not (funcao.acaba_jogo(log_posicao_navios_computador)):
        print('O {} ganhou essa! Parabéns'.format(NOME_JOGADOR))
        jogo = False
    else:
        jogo = True