from random import randint

print('JOGO DA VELHA')
print('''
_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9 ''')
print('\n\n')

class Game:
    def __init__(self, player='X', bot='O'):
        self.player = player[0]
        self.bot = str('#' if bot == player else bot)[0]
        self.player_pos = []
        self.bot_pos = []
        self.game_pos = []
        self.local = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    def mainloop(self):
        while True:
            resp = int(input('>>> '))

            # Calcular e criar posição do jogador
            break_ = False
            b = False
            for n in self.local:
                if break_ == True : break
                if resp == n:
                    if not resp in self.game_pos:
                        self.player_pos.append(n)
                        self.game_pos.append(n)
                        break_ = True
                    else:
                        print(f'Posição {resp} já foi usada...Tente novamente')
                        b = True

            # Fim de jogo
            # Como o player sempre vai dá o ultimo movimento, o fim de jogo vem primeiro que o bot 
            if len(self.game_pos) == 9:
                print('\n\nFIM DE JOGO!')
                vitorias = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
                    
                for _ in vitorias:
                    if _[0] in self.player_pos and _[1] in self.player_pos and _[2] in self.player_pos:
                        print(f'Jogador {self.player} GANHOU!')
                        break
                    
                for _ in vitorias:
                    if _[0] in self.bot_pos and _[1] in self.bot_pos and _[2] in self.bot_pos:
                        print(f'Jogador {self.bot} GANHOU!')
                        break
                    
                self.player_pos = []
                self.bot_pos = []
                self.game_pos = []
                self.mainloop()
                break

            # Calcular e criar posição do bot
            break_ = b      
            bot = randint(1, 9)
            while True:
                if break_ == True : break
                for n in self.local:
                    if break_ == True : break
                    if bot == n:
                        if break_ == True : break
                        if not bot in self.game_pos:
                            self.bot_pos.append(n)
                            self.game_pos.append(n)
                            break_ = True
                        else:
                            bot = randint(1, 9)
                    else:
                        bot = randint(1, 9)
                        
                  
            # Aparecer o jogo no terminal
            format = ''
            for i in range(0, 9, 3):  
                el1 = el2 = el3 = ' '

                linha = self.local[i:i+3]  

                elementos = []
                for pos in linha:
                    if pos in self.player_pos:
                        elementos.append(self.player)
                    elif pos in self.bot_pos:
                        elementos.append(self.bot)
                    else:
                        elementos.append(' ')

                line = f' {elementos[0]} | {elementos[1]} | {elementos[2]} '
                format += line + '\n'
                if i < 6:
                    format += "---|---|---\n"

            print(format)

            # Calcular a vitoria do jogo
            vitorias = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
                
            for _ in vitorias:
                if _[0] in self.player_pos and _[1] in self.player_pos and _[2] in self.player_pos:
                    print(f'Jogador {self.player} GANHOU!')
                    self.player_pos = []
                    self.bot_pos = []
                    self.game_pos = []
                    self.mainloop()
                    break
                
            for _ in vitorias:
                if _[0] in self.bot_pos and _[1] in self.bot_pos and _[2] in self.bot_pos:
                    print(f'Jogador {self.bot} GANHOU!')
                    self.player_pos = []
                    self.bot_pos = []
                    self.game_pos = []
                    self.mainloop()
                    break
                    

                    

if __name__ == '__main__':
    game = Game(player='X', bot='O') # Qualquer caracteres 

    game.mainloop()
