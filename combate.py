import random
from batalha import Batalha
from util import Util

class Combate():
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.batalha = Batalha()

    def dados_idimigo(self, personagem2):
        dados_inimigo = random.randint(1,10)
        if personagem2.vidabase > personagem2.vida * 0.3:
            if dados_inimigo > 5:
                return 1  
            else:
                return 2
        else:
            if dados_inimigo > 3:
                return 1 
            else:
                return 2 

    def combate_pratico(self):
            turno = 1
            
            while self.p1.vida > 0 or self.p2.vida > 0:
                
                print(f'\n===== TURNO {turno} =====')
                numero1 = 0
                while numero1 not in [1, 2, 3]:
                    print('Escolha o numero desejado:')
                    print('1 - Para atacar       2 - Para se defender        3 - Para usar poção')
                    try:
                        numero1 = int(input("Escolha o numero: ")) 
                        if numero1 not in [1, 2, 3]:
                            print('Opção inválida, tente novamente (1, 2 ou 3).')
                    except ValueError:
                        print('Entrada inválida. Digite 1, 2 ou 3.')

                numero2 = self.dados_idimigo(self.p2)

                if numero1 == 1 and numero2 == 2:
                    
                    self.batalha.atacar(self.p1, self.p2) 
                    
                elif numero1 == 2 and numero2 == 1:
                    
                    self.batalha.atacar(self.p2, self.p1)
                    
                elif numero1 == 1 and numero2 == 1:
                    
                    self.batalha.atacar_sem_defesa(self.p1, self.p2)
                    self.batalha.atacar_sem_defesa(self.p2, self.p1)

                elif numero1 == 2 and numero2 == 2:
                
                    self.batalha.ambos_defende()

                elif numero1 == 3:
                    
                    self.batalha.usar_pocao(self.p1, self.p1.itens)
                    if numero2 == 1:
                        self.batalha.atacar(self.p2, self.p1)
                    else: 
                        print(f'{self.p2.nome} defende enquanto {self.p1.nome} usa poção.')
                
                if self.p2.vida <= 0:
                    print(f'personagem{self.p2}foi derrotado')
                    break
                
                if self.p1.vida <= 0:
                    print(f'personagem{self.p1}foi derrotado')
                    break
                
                turno += 1