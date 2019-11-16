from random import randint
import os

class forca():
    def __init__(self):
        self.chave = ""
        self.erros = 0
        self.acertos = ""
        self.palavraFinal = ""
        self.palavra = self.chamaPalavra()
        
        


    def chamaPalavra(self):
        self.palavra = input("Escolha a palavra: ")
        os.system("cls")
        for i in self.palavra:
            self.chave += "- "
        self.inicializando()

    def inicializando(self):
        print(f"{len(self.palavra)} letras! \n" + self.chave)

        while self.erros < 4:
            def winnerCheck(x):
                    if x == self.palavra:
                        ganhou()
                    else:
                        pass

            def ganhou():
                print(f"Você Ganhou! a palavra é {self.palavra}")
                if self.erros == 0:
                    desenho("winner")
                if self.erros == 1:
                    desenho("winner2")
                if self.erros == 2:
                    desenho("winner3")
                if self.erros == 3:
                    desenho("winner4")
                exit(123)


            def desenho(x):
                if x == 0:
                    print('''
___________________|
		|
                |
               ( ) 
                |
               /|\ 
                | 
                ^
               / \ 


                    ''')
                if x == 1:
                    print('''       
_________________|
		|
                |
               ( )
                |
               /|\ 
                |
                ^
               / 
você perdeu a perna esquerda :c
                    
                    ''')
                if x == 2:
                    print('''       
_________________|
		|
                |
               ( )
                |
               /|\ 
                |
                
               
você está alejado
                    
                    ''')
                if x == 3:
                    print('''       
_________________|
		|
                |
               ( )
                |
               /|
                |

você perdeu um dos braços e está alejado, mas ainda consegue\nsobreviver com um braço
                    ''')
                if x == 4:
                    print('''       
_________________|
		|
                |
               ( )
                |
                |
                |

você virou um cotoco e morreu sufocado
                    ''')
                if x == "winner":
                    print('''
____________________|
                                     __     __          __          ___       
               ( )                   \ \   / /          \ \        / (_)      
               \|/                    \ \_/ /__  _   _   \ \  /\  / / _ _ __  
                |                      \   / _ \| | | |   \ \/  \/ / | | '_ \ 
                ^                       | | (_) | |_| |    \  /\  /  | | | | |
               / \                      |_|\___/ \__,_|     \/  \/   |_|_| |_|


                                            
                    ''')
                if x == "winner2":
                    print('''
____________________|
                                     __     __          __          ___       
               ( )                   \ \   / /          \ \        / (_)      
               \|/                    \ \_/ /__  _   _   \ \  /\  / / _ _ __  
                |                      \   / _ \| | | |   \ \/  \/ / | | '_ \ 
                ^                       | | (_) | |_| |    \  /\  /  | | | | |
               /                        |_|\___/ \__,_|     \/  \/   |_|_| |_|

                    ''')
                if x == "winner3":
                    print('''
____________________|
                                     __     __          __          ___       
               ( )                   \ \   / /          \ \        / (_)      
               \|/                    \ \_/ /__  _   _   \ \  /\  / / _ _ __  
                |                      \   / _ \| | | |   \ \/  \/ / | | '_ \ 
                                        | | (_) | |_| |    \  /\  /  | | | | |
                                        |_|\___/ \__,_|     \/  \/   |_|_| |_|

            
                    ''')
                if x == "winner4":
                    print('''
____________________|
                                     __     __          __          ___       
               ( )                   \ \   / /          \ \        / (_)      
               \|                    \ \_/ /__  _   _   \ \  /\  / / _ _ __  
                |                      \   / _ \| | | |   \ \/  \/ / | | '_ \ 
                                        | | (_) | |_| |    \  /\  /  | | | | |
                                        |_|\___/ \__,_|     \/  \/   |_|_| |_|

            
                    ''')

            desenho(self.erros)
        
            res = input()
            
            if res == self.palavra:
                ganhou()
                
                
                
            

            

            

            if res in self.palavra:
                self.acertos += res
                self.chave = ""
                self.palavraFinal = ""

                for i in self.palavra:
                    if i in self.acertos:
                        self.chave += i + " "
                        
                        
                    else:
                        self.chave += "- "
                self.palavraFinal = self.chave.replace(" ", "")
                print("\n" +self.chave)
                winnerCheck(self.palavraFinal)
            

            else:
                print(f"\n\nA letra {res} não está na palavra :c\n")
                self.erros += 1
        else:
            print(f"A palavra era {self.palavra}")
            desenho(self.erros)
            exit(123)
forca()