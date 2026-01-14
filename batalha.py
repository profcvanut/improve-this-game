import random
from util import Util
from colorama import Fore, Style, init

init(autoreset=True)

class Batalha:
    def __init__(self):
        pass

    def atacar(self, atacante, defensor):
        dano = max(0, atacante.ataque - defensor.defesa)
        defensor.vida -= dano
        if defensor.vida <= dano:
            defensor.vida = 0
        print(f'{atacante.nome} ataca {defensor.nome} causando {dano} de dano! {defensor.nome} agora tem {defensor.vida} de vida.')
        Util.pausa(2)

    def atacar_sem_defesa(self, atacante, defensor):
        dano = atacante.ataque
        defensor.vida -= dano
        if defensor.vida <= dano:
            defensor.vida = 0
        print(f'{atacante.nome} ataca {defensor.nome} diretamente, causando {dano} de dano! {defensor.nome} agora tem {defensor.vida} de vida.')
        Util.pausa(2)

    def ambos_defende(self):
        print('Ambos os personagens se defendem! Nada acontece neste turno.')
        Util.pausa(2)

    def usar_pocao(self, personagem, itens):
        print('Poções disponíveis:')
        print('1 - ' + Fore.YELLOW + 'Poção vermelha' + Fore.WHITE + f' (Qtd: {itens[0]["qnt"]})')
        print('2 - ' + Fore.BLUE + 'Poção azul' + Fore.WHITE + f' (Qtd: {itens[1]["qnt"]})')
        print('3 - ' + Fore.GREEN + 'Poção verde' + Fore.WHITE + f' (Qtd: {itens[2]["qnt"]})')
        try:
            opcao = int(input('Selecione a poção que deseja usar: '))
        except ValueError:
            print(Fore.RED + 'Você não selecionou uma das opções de poções válidas!' + Fore.RESET)
            Util.pausa(2)
            return

        if opcao == 1:
            if itens[0]['qnt'] > 0:
                itens[0]['qnt'] -= 1
                personagem.vida += 30
                if personagem.vida > personagem.vidabase:
                    personagem.vida = personagem.vidabase
                print(Fore.GREEN + f'{personagem.nome} usou uma poção vermelha e recuperou 30 de vida! Vida atual: {personagem.vida}.' + Fore.RESET)
            else:
                print(Fore.RED + 'Suas poções vermelhas acabaram!' + Fore.RESET)
        elif opcao == 2:
            if itens[1]['qnt'] > 0:
                itens[1]['qnt'] -= 1
                personagem.ataque += 10
                print(Fore.GREEN + f'{personagem.nome} usou uma poção azul e aumentou seu ataque em 10! Ataque atual: {personagem.ataque}.' + Fore.RESET)
            else:
                print(Fore.RED + 'Suas poções azuis acabaram!' + Fore.RESET)
        elif opcao == 3:
            if itens[2]['qnt'] > 0:
                itens[2]['qnt'] -= 1
                personagem.defesa += 10
                print(Fore.GREEN + f'{personagem.nome} usou uma poção verde e aumentou sua defesa em 10! Defesa atual: {personagem.defesa}.' + Fore.RESET)
            else:
                print(Fore.RED + 'Suas poções verdes acabaram!' + Fore.RESET)
        else:
            print(Fore.RED + 'Opção de poção inválida.' + Fore.RESET)
        Util.pausa(2)
        def recuperar_estatos_completo(self, personagem):
            personagem.vida = personagem.vidabase
            personagem.ataque = personagem.ataquebase
            personagem.defesa = personagem.defesabase
            return personagem.defesa, personagem.ataque, personagem.vida
        def repurar_estatos_posbatalha(self, personagem):
            personagem.ataque = personagem.ataquebase
            personagem.defesa = personagem.defesabase
            return personagem.defesa, personagem.ataque