# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            
    def r1(self):
        # R1 - Com duas marcacoes em sequencia, ataque ou defenda
        coordenada_vazia = Tabuleiro.DESCONHECIDO

        # ATAQUE 
        for i in range(3):  # linhas
            linha = self.matriz[i]
            soma = sum(linha)
            if soma == 8 and coordenada_vazia in linha:
                print(f"Atacando na linha {i}")
                return (i, linha.index(coordenada_vazia))

        for j in range(3):  # colunas
            coluna = [self.matriz[i][j] for i in range(3)]
            soma = sum(coluna)
            if soma == 8 and coordenada_vazia in coluna:
                print(f"Atacando na coluna {j}")
                return (coluna.index(coordenada_vazia), j)

        diagonal1 = [self.matriz[i][i] for i in range(3)]
        soma = sum(diagonal1)
        if soma == 8 and coordenada_vazia in diagonal1:
            print(f"Atacando diagonal1 na posição {loc}")
            loc = diagonal1.index(coordenada_vazia)
            return (loc, loc)

        diagonal2 = [self.matriz[i][2 - i] for i in range(3)]
        soma = sum(diagonal2)
        if soma == 8 and coordenada_vazia in diagonal2:
            print(f"Atacando diagonal2 na posição {loc}")
            loc = diagonal2.index(coordenada_vazia)
            return (loc, 2 - loc)

        # DEFESA 
        for i in range(3):  # linhas
            linha = self.matriz[i]
            soma = sum(linha)
            if soma == 2 and coordenada_vazia in linha:
                print(f"Defendendo na linha {i}")
                return (i, linha.index(coordenada_vazia))

        for j in range(3):  # colunas
            coluna = [self.matriz[i][j] for i in range(3)]
            soma = sum(coluna)
            if soma == 2 and coordenada_vazia in coluna:
                print(f"Defendendo na coluna {j}")
                return (coluna.index(coordenada_vazia), j)

        soma = sum(diagonal1)
        if soma == 2 and coordenada_vazia in diagonal1:
            print(f"Defendendo diagonal1 na posição {loc}")
            loc = diagonal1.index(coordenada_vazia)
            return (loc, loc)

        soma = sum(diagonal2)
        if soma == 2 and coordenada_vazia in diagonal2:
            print(f"Defendendo diagonal2 na posição {loc}")
            loc = diagonal2.index(coordenada_vazia)
            return (loc, 2 - loc)

        return None
    
    def r2(self):
        # R2 - Jogada que proporciona duas sequencias de marcacao
        coordenada_vazia = Tabuleiro.DESCONHECIDO
        tipo = self.tipo

        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == coordenada_vazia:
                    self.matriz[l][c] = tipo  # simula jogada
                    
                    cont = 0
                    
                    if self.matriz[l].count(tipo) == 2 and self.matriz[l].count(coordenada_vazia) == 1:
                        cont += 1
                    
                    coluna = [self.matriz[i][c] for i in range(3)]
                    if coluna.count(tipo) == 2 and coluna.count(coordenada_vazia) == 1:
                        cont += 1
                    
                    if l == c:
                        diagonal1 = [self.matriz[i][i] for i in range(3)]
                        if diagonal1.count(tipo) == 2 and diagonal1.count(coordenada_vazia) == 1:
                            cont += 1
                    
                    if l + c == 2:
                        diagonal2 = [self.matriz[i][2 - i] for i in range(3)]
                        if diagonal2.count(tipo) == 2 and diagonal2.count(coordenada_vazia) == 1:
                            cont += 1
                    
                    self.matriz[l][c] = coordenada_vazia  # desfaz simulação
                    
                    if cont >= 2:
                        return (l, c)
        return None

    def r3(self):
        # R3 - Marcar quadrado central
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        return None

    def r4(self):
        # R4 - Marcar canto oposto do oponente
        oponente = 1 if self.tipo == 4 else 4  # se você é 4, oponente é 1 e vice-versa
        coordenada_vazia = Tabuleiro.DESCONHECIDO

        cantos = [ (0,0), (0,2), (2,0), (2,2) ]
        cantos_opostos = { (0,0):(2,2), (0,2):(2,0), (2,0):(0,2), (2,2):(0,0) }

        for canto in cantos:
            l, c = canto
            oposto_l, oposto_c = cantos_opostos[canto]

            if self.matriz[l][c] == oponente and self.matriz[oposto_l][oposto_c] == coordenada_vazia:
                return (oposto_l, oposto_c)

        return None

    def r5(self):
        # R5 - Marcar canto vazio
        coordenada_vazia = Tabuleiro.DESCONHECIDO
        cantos = [(0,0), (0,2), (2,0), (2,2)]

        for l, c in cantos:
            if self.matriz[l][c] == coordenada_vazia:
                return (l, c)

        return None

    def r6(self):
        # R6 - Jogada Aleatoria:
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None

    def getJogada(self) -> (int, int):
        for regra in [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6]:
            jogada = regra()
            if jogada is not None:
                return jogada
        return None






        



