# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        i = 0

        for i in range(3):
            # != 0 garante que nao ta considerando espaco vazio
            if (self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] != 0):
                # pegar o codigo do vencedor (qualquer uma das tres posicoes)
                vencedor_code = self.matriz[i][0]
                # operacao ternaria so para printar no stdout a string correta do vencedor
                print(vencedor_code, "venceu na horizontal")
                # retorna o valor do jogador ganhador
                return vencedor_code

            if (self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] != 0):
                vencedor_code = self.matriz[0][i]
                print(vencedor_code, "venceu na vertical")
                return vencedor_code

        if (self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != 0):
                vencedor_code = self.matriz[0][0]
                print(vencedor_code, "venceu na diagonal 1")
                return vencedor_code

        if (self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != 0):
            vencedor_code = self.matriz[0][2]
            print(vencedor_code, "venceu na diagonal 2")
            return vencedor_code 

        return 0

            

