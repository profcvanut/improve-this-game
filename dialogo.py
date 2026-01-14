from colorama import Fore, Style, init
from util import Util
from personagem import Personagem
from combate import Combate

init(autoreset=True)

texto = '''Ninguém sabe seu nome.
Alguns o chamam de “o Estranho da Capa Cinzenta”, outros apenas “o Herói Sem Nome”.
Tudo o que sesabe é que ele surgiu quando o Reino de Eldoria mergulhou na escuridão.

Há poucas luas, a Princesa Althea foi raptada por Lord Vharok, um feiticeiro que domina as sombras e comanda um exército de criaturas corrompidas.
Dizem que Vharok pretende usar o sangue da princesa em um antigo ritual, capaz de abrir o Portal das Trevas Eternas.

Sem rei, sem exército, o povo caiu no desespero.
Mas o herói sem nome — empunhando apenas uma espada enferrujada e uma coragem inexplicável — decide partir em busca da princesa.

Sua jornada começa nas ruínas da antiga fortaleza de Eldoria, atravessando florestas amaldiçoadas, montanhas geladas e catacumbas cheias de perigos.
A cada passo, ele precisa melhorar sua força, encontrar poções e enfrentar criaturas que tentam impedi-lo de chegar ao Castelo Sombrio — onde Vharok o aguarda.

Dizem que, se o herói triunfar, seu nome será finalmente revelado.
Mas se falhar... Eldoria desaparecerá nas trevas para sempre.'''
dialogos_edran = [{'decisao1': '''O ar é frio e úmido quando você deixa o vilarejo para trás.
A trilha de pedras se estreita até se perder sob raízes antigas, e logo o som das corujas e do vento domina o silêncio.

A Floresta de Auren é conhecida por dois motivos:
por ser o refúgio de antigos magos — e o túmulo dos tolos que tentaram caçá-los.

A cada passo, a luz do dia se desfaz em fragmentos, filtrada por galhos retorcidos.
Há algo de vivo nas árvores. Algo que observa.

Você sente o chão pulsar sob as botas, como se a própria floresta respirasse ao seu redor.

Então, uma voz rompe o silêncio — calma, mas firme, ecoando como se viesse de todos os lados.

???
“Poucos entram em Auren sem ser convidados.
E menos ainda saem daqui sem deixar algo para trás…”

Uma figura encapuzada surge entre as névoas, segurando um cajado de madeira prateada.
O brilho em seus olhos não é de ameaça, mas de julgamento.

Assim, o destino o coloca diante de Edran, o Mago do Crepúsculo.'''},
{'edran_vilao': '''Edran:
Você achou mesmo que eu ajudaria um tolo sem nome?

Edran:
Foi você quem abriu o portal, há muito tempo.
Eu só… continuei o que começamos juntos.

Herói:
Mentira! Eu jamais trairia Althea!

Edran:
Não lembra?
Você a entregou a mim, de bom grado.
Agora, cumpra seu destino — e torne-se sombra!'''}, 
{'edran_apice_corrupicao': '''Edran:
Silêncio… consegue ouvir? O som do poder me chamando.
Eu o contive por tanto tempo… e para quê? Por causa da luz? Da esperança?

Herói:
Edran… o que está dizendo?

Edran:
Que o bem é uma prisão, e eu cansei de ser prisioneiro.
Passei a vida guiando tolos como você, acreditando em redenção…

Edran (voz distorcida):
Mas o que é a redenção, se não o medo de ser quem realmente somos?

Herói:
Isso não é você…

Edran:
Pelo contrário, agora sou eu.
Sem máscaras. Sem limites.
E quando o mundo queimar, o meu nome será o vento que o consome.'''}]
dialogos_kael = [
{'kael_vilao': '''Kael:
Você sempre foi ingênuo, herói.

Kael:
Enquanto lutava por amor e honra, eu lutava por algo real: poder.

Herói:
Então era isso… desde o início.

Kael:
Vharok me ofereceu um trono.
E eu aceitei.

Kael:
Afinal, um homem precisa de um nome…
E o meu será gravado nas cinzas do seu.'''},
{'kael_apice_corrupicao': '''Kael:
Sabe o que aprendi, herói?
Lealdade é só a desculpa dos fracos pra não trair primeiro.

Herói:
Kael… não faça isso.

Kael:
Você fala como se houvesse escolha.
Desde o início, o ouro, o sangue e o medo foram meus verdadeiros deuses.

Herói:
Você enlouqueceu.

Kael (rindo):
Não… eu despertei.
E finalmente, vou tomar tudo que o destino te prometeu.'''}]
Edran_decisao = [{'decisao1': '''
Entre os escombros de uma vila queimada, prisioneiros ajoelham-se diante das chamas. Edran os observa, o rosto dividido entre raiva e pena.

Edran:
Eles mataram e roubaram… mas agora pedem clemência.
O que você faria, herói? Justiça ou misericórdia?
'''},
{'decisao2': '''No coração da floresta, uma criança de olhos negros dorme, cercada por símbolos de um ritual sombrio. O ar vibra com energia arcana.

Edran:
A corrupção toca até os inocentes.
Posso purificar a criança, mas se falhar… o demônio nela despertará.
O que devo fazer?
'''},
{'decisao3': '''Um artefato antigo repousa sobre o altar — pulsante, vivo, quase consciente. A sala inteira sussurra promessas de poder.

Edran:
Com este artefato, posso destruir Vharok…
ou me tornar algo pior que ele.

Herói:
O poder é sempre uma escolha.

Edran:
Então escolha comigo.
'''},
{'decisao4': '''Dentro de um cristal flutua um espírito aprisionado — metade luz, metade sombra. A voz ecoa: “Liberta-me, e libertarei o mundo.”

Edran:
Já ouvi essa promessa antes.
E o mundo sangrou por causa dela.
'''},
{'decisao5': '''O castelo de Vharok cai em ruínas. O céu brilha em fogo e cinza.
Diante do trono vazio, Edran ergue o cajado, e o poder primordial pulsa em suas veias.

Edran:
O trono está vazio…
Com um gesto, posso restaurar a luz — ou fazer o mundo me obedecer.

Herói:
Então o que vai escolher?
'''}]
kael_decisao = [{'decisao1': '''Um espião capturado implora por sua vida.
Kael o observa com olhos frios, a espada pendendo na altura do pescoço do homem.

Kael:
Ele sabe coisas. Pode nos ajudar… ou trair de novo.
O que você faria?
'''},
{'decisao2': '''O fogo consome as casas. Gritos ecoam ao longe. Kael olha indeciso — salvar civis ou atacar a base inimiga?

Kael:
Podemos salvar os aldeões… ou acabar com os inimigos de uma vez.
Mas não dá pra fazer os dois.
'''},
{'decisao3': '''Um carregamento de ouro roubado dos cofres do exército inimigo está diante de vocês.
Kael segura um punhado de moedas, pensativo.

Kael:
Com isso, poderíamos reconstruir metade do reino…
ou nunca mais precisar lutar.
'''},
{'decisao4': '''Em uma cripta antiga, uma espada repousa sobre ossos queimados.
Ela sussurra o nome de Kael.

Kael:
Dizem que essa lâmina bebe a alma de quem a empunha…
Mas corta até a carne dos demônios.
'''},
{'decisao5': '''A guerra terminou. O reino está em ruínas. Kael observa o horizonte, a espada cravada no chão.

Kael:
Podemos reconstruir… ou deixar tudo queimar e começar de novo.
O que você faria, herói?
'''}]
caminho1 = [{'caminho1_floresta': '''O ar da floresta é frio, como se o tempo tivesse parado.
A bruma dança entre as árvores, e os galhos sussurram segredos antigos.

No centro do bosque, uma figura encapuzada se ergue diante de um círculo de pedra.

Edran:
“Auren raramente aceita visitantes.
O que te traz até onde até os deuses se calam?”

Herói:
“Procuro a princesa Althea. Dizem que o rei Vharok a levou para o Castelo Sombrio.”

Edran:
“Então o ciclo se repete.
Luz e sombra se movem como marés, mas poucos percebem qual lado estão alimentando.”

Ele o observa em silêncio.

Edran:
“Siga o norte.
Mas lembre-se: há caminhos que levam à vitória… e outros à ruína — e às vezes são o mesmo.”

Edran, curioso sobre como o desconhecido seguiria seu caminho, decide acompanhá-lo durante a sua jornada'''},
{'caminho1_estrada': '''O Herói, após seu árduo percurso, encontra-se na chamada estrada de Kareth. 
A estrada de Kareth é árida e cruel.
O som distante de espadas ecoa nas colinas, e a poeira do solo parece tingida de sangue antigo.

Um guerreiro observa as ruínas com o olhar de quem já perdeu mais do que ganhou.

Kael:
“Você vem da floresta, não é?
Ouvi dizer que um mago vagueia por lá, falando em destino e espelhos.
Aposto que ele te encheu de dúvidas.”

Herói:
“Ele me mostrou o caminho.”

Kael:
“Ou te colocou em um labirinto.
Os magos gostam de brincar com os outros — e com o próprio passado.”

Ele se aproxima, baixando a espada.

Kael:
“Se realmente vai atrás da princesa, lembre-se: o castelo de Vharok não é um lugar para sonhadores.
Só sobrevivem os que sabem o que estão dispostos a sacrificar.”

Ele dá um passo para o lado e abre caminho.

Kael:
“Vá. O destino te observa… mas ele também sangra.”'''}]
caminho2 = [{'caminho2_estrada': '''O vento açoita o chão seco de Kareth.
O céu pesa como ferro, e o som distante de ferros batendo ecoa por entre as ruínas.

Um guerreiro limpa o sangue de sua espada e o encara em silêncio.

Kael:
“Um viajante? Ou mais um tolo em busca de glória?”

Herói:
“Busco a princesa Althea. Dizem que o rei Vharok a mantém prisioneira.”

Kael:
“Então vai até o norte.
O castelo te espera… e ele não tem pressa em devorar esperanças.”

Ele embainha a espada, mas não tira o olhar de você.

Kael:
“Se chegar até lá, lembre-se: coragem é boa, mas não substitui sabedoria.”'''},
{'caminho2_floresta': '''A floresta o recebe em silêncio.
Cada passo sobre as folhas úmidas ecoa como um sussurro distante.

Um círculo de luz brilha entre as raízes, e dele surge uma figura de olhos intensos.

Edran:
“Ah… o guerreiro de Kareth.
O cheiro de ferro denuncia suas escolhas.”

Herói:
“Procuro o caminho até o Castelo Sombrio.”

Edran:
“Todos procuram algo lá.
Uns querem poder, outros redenção… e alguns apenas buscam se esquecer.”

Ele o observa por alguns instantes.

Edran:
“A estrada o mudou, mas não o definiu — ainda há tempo.
Se quiser salvar a princesa, precisará primeiro salvar a si mesmo.”

A bruma se levanta, envolvendo-o.
Quando você olha de novo, Edran já se foi —
mas o chão onde ele estava brilha com runas que apontam para o norte.'''}]
finais = [{'Bom': '''Narrador:
O Herói e seus aliados, Edran e Kael, chegam ao Castelo Sombrio. Juntos, o poder da magia, a força da honra e a determinação do Herói triunfam sobre Lord Vharok. A Princesa Althea é salva, e o Reino de Eldoria é restaurado. Os três se tornam lendas, provando que a verdadeira força reside na união.

Edran:
A Bondade nos salvou, herói.

Kael:
E a coragem de não ter desistido de nós.

Narrador:
O herói sem nome finalmente recebe seu nome, gravado na história como o salvador do reino.'''},
{'medio_edran': '''Narrador:
Edran se foi, consumido pela própria magia. Kael e o Herói prosseguem. Sem a sabedoria do mago, a batalha é mais difícil, mas a força de Kael garante a vitória. A Princesa Althea é salva, mas o custo da redenção de Edran paira sobre o reino.

Kael:
Ele morreu como viveu… dizendo palavras que ninguém entendia. Mas cumpriu sua parte.

Herói:
E agora, o que faremos sem sua orientação?

Kael:
Lutamos. Como sempre fizemos.'''},
{'medio_kael': '''Narrador:
Kael caiu em batalha, e o silêncio da estrada pesa como uma promessa quebrada. Edran e o Herói chegam ao castelo. A força do mago é essencial, mas a falta da lâmina de Kael é sentida. Eles triunfam, mas a vitória é agridoce.

Edran:
Kael era um homem de honra, mesmo que a escondesse.

Herói:
Eu devia ter lutado por ele...

Edran:
O destino escolheu o caminho, Herói. Agora, honre a memória dele reconstruindo o que ele ajudou a salvar.'''},
{'ruim': '''Narrador:
O herói vagueia sozinho. A estrada está vazia, e as vozes de Edran e Kael ecoam apenas na memória. O reino, sem líderes, sem aliados e sem esperança, é consumido pelas trevas. A Princesa Althea permanece prisioneira, e Lord Vharok finalmente abre o Portal das Trevas Eternas.

Herói:
Eu falhei...

Voz de Edran (eco):
“A escuridão triunfa quando a luz hesita.”

Voz de Kael (eco):
“Ninguém vence sozinho, tolo.”

Narrador:
E assim, o Herói Sem Nome desaparece nas sombras, lembrado apenas como o homem que quase salvou Eldoria.'''}]


class Dialogos:
    def __init__(self, dialogo, heroi, edran, kael):
        self.dialogo = dialogo
        self.heroi = heroi
        self.edran = edran
        self.kael = kael
        self.finais = finais
        self.Edran_decisao = Edran_decisao
        self.kael_decisao = kael_decisao
        self.caminho1 = caminho1
        self.caminho2 = caminho2

    def introducao(self):
        Util.limpar_tela()
        texto_recortado = self.dialogo.split()
        texto_junto = ' '.join(texto_recortado)
        cont = 0
        for i in texto_junto:
            print(i, end='')
            Util.pausa(0.05)
            cont = cont + 1
            if cont % 120 == 0:
                print('-\n')
        print('\n')
        Util.continuar()
        self.escolha_caminho()

    def heroi_entrada(self):
        pass

    def dialogo_heroi_npc(self, dialogo):
        Util.limpar_tela()
        cont = 0
        for i in dialogo:
            print(i, end='')
            Util.pausa(0.05)
            cont = cont + 1
        print('\n')
        Util.continuar()

    def decisao_edran(self):
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Mini-Jornada com Edran'))
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 1'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(Edran_decisao[0]['decisao1'])
        print('Opções:')
        print('1 - Perdoe-os. Ninguém nasce corrompido, apenas perdido.\n2 - Deixe-os partir. O tempo cuidará de puni-los ou curá-los.\n3 - Eles escolheram o caos. Dê-les o destino que buscaram.')
        try:
            self.opcao = int(input('Insira a sua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.edran)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 2'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(Edran_decisao[1]['decisao2'])
        print('1 - Arrisque. Toda alma merece uma chance, mesmo que custe a nossa.')
        print('2 - Espere. Se for realmente inocente, sobreviverá sem intervenção.')
        print('3 - Acabe logo com isso. A piedade é um luxo perigoso.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.edran)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 3'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(Edran_decisao[2]['decisao3'])
        print('1 - Destrua-o. O mundo precisa de sabedoria, não de força.')
        print('2 - Guarde-o. Talvez ainda haja um propósito equilibrado.')
        print('3 - Use-o. Melhor o poder estar conosco do que contra nós.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.edran)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 4'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(Edran_decisao[3]['decisao4'])
        print('1 - Libere-o. Mesmo a escuridão pode se arrepender.')
        print('2 - Deixe-o. Nem toda prisão é injusta.')
        print('3 - Absorva o poder dele. Faça com que sirva ao bem — ou ao mal.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.edran)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 5'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(Edran_decisao[4]['decisao5'])
        print('1 - Restaure o equilíbrio. O mundo precisa de cura, não domínio.')
        print('2 - Não decida nada. O tempo é o único juiz verdadeiro.')
        print('3 - Sente-se no trono. Governe as sombras.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.edran)

    def decisao_kael(self):
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Mini-Jornada com Kael'))
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 1'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(kael_decisao[0]['decisao1'])
        print('Opções:')
        print('1 - Poupe-o. O perdão às vezes vale mais que a confissão\n2 - Prenda-o. Justiça não é morte, é vigilância.\n3 - Mate-o. A traição não precisa de segunda chance.')
        try:
            self.opcao = int(input('Insira a sua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.kael)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 2'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(kael_decisao[1]['decisao2'])
        print('1 - Salve-os. O heroísmo não se mede em vitórias, mas em vidas salvas.\n2 - Siga o plano. O campo de batalha decide, não o coração\n3 - Ignore-os. A vitória vale mais que algumas vidas.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.kael)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 3'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(kael_decisao[2]['decisao3'])
        print('1 - Distribua o ouro entre os sobreviventes. Eles precisam mais que nós\n2 - Guarde-o. O futuro é incerto.\n3 - Pegue tudo. O mundo nos deve pelo sangue derramado.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.kael)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 4'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(kael_decisao[3]['decisao4'])
        print('1 - Deixe-a. Nenhuma vitória vale a tua alma.\n2 - Leve-a. Use apenas se não houver escolha\n3 - Empunhe-a. Se é maldita, que tema o teu nome.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.kael)
        Util.limpar_tela()
        Util.separacao_cabecalho()
        print('{:^70}'.format('Jornada 5'))
        Util.separacao_cabecalho()
        self.dialogo_heroi_npc(kael_decisao[4]['decisao5'])
        print('1 - Reconstrua. A força que destrói também pode erguer\n2 - Deixe os vivos decidirem o próprio caminho.\n3 - Destrua o que restou. O mundo só renasce após morrer.')
        try:
            self.opcao = int(input('\nSua escolha: '))
        except ValueError:
            self.opcao = 0
        self.condicionais(self.opcao, self.kael)

    def condicionais(self, opcao, npc_alvo):
        if opcao == 1:
            self.heroi.update_bondade(3)
            npc_alvo.update_bondade(1)
            
        elif opcao == 2:
            self.heroi.update_bondade(1)
            
        elif opcao == 3:
            self.heroi.downgrade_bondade(3)
            npc_alvo.downgrade_bondade(1)
            
        else:
            print(Fore.RED + 'Você selecinou uma opção inválida!' + Fore.RESET)
            Util.pausa(2)
            return
        
    def aplicar_consequencia_individual(self, npc):
        
        Util.limpar_tela()
        
        dialogo_recompensa_edran = '''Edran:
Sua luz é inegável, herói. Você provou que a bondade ainda é uma força.
Pegue isso. Considere um presente de um velho mago a um jovem de bom coração.'''
        dialogo_recompensa_kael = '''Kael:
Você me surpreendeu. Sua honestidade e força me fazem lembrar por que eu lutava.
Aqui, use isso com sabedoria, e que isso te mantenha no caminho da honra.'''
        dialogo_confronto_edran = '''Edran:
Seu caminho não é fácil, nem sua alma é pura. Estamos em equilíbrio.
Mas o portal sombrio não espera. Você me julgará com sua espada e forçará um fim, ou me dará a chance de buscar a redenção por mim mesmo?'''
        dialogo_confronto_kael = '''Kael:
Você não é tolo o bastante para ser ingênuo, nem frio o suficiente para ser um vilão.
Nós dois andamos na beira. Você me vê como um aliado ou como apenas mais um obstáculo?
Escolha agora.'''

        print(Fore.CYAN + f"\nA Bondade final de {npc.nome} é: {npc.bondade}" + Fore.RESET)
        Util.pausa(2) 
        
        if self.heroi.bondade == 10:
            self.dialogo_heroi_npc(dialogo_recompensa_edran if npc.nome == 'Edran' else dialogo_recompensa_kael)
            self.heroi.ganhar_itens()
            npc.estatos = 1
            print(Fore.GREEN + f"Você ganhou 2 poções de cada tipo! Inventário atualizado." + Fore.RESET)
            Util.continuar()
            
        elif self.heroi.bondade == -10:
            self.dialogo_heroi_npc(dialogos_edran[1]['edran_vilao'] if npc.nome == 'Edran' else dialogos_kael[0]['kael_vilao'])
            
            print(Fore.RED + f'\n{npc.nome} se volta contra você! O combate é inevitável.' + Fore.RESET)
            Util.continuar()
            
            self.heroi.vida = self.heroi.vidabase
            npc.vida = npc.vidabase
            
            combate = Combate(self.heroi, npc)
            combate.combate_pratico()

            if npc.vida <= 0: 
                npc.estatos = 2
                print(Fore.GREEN + f'\n{npc.nome} foi derrotado.' + Fore.RESET)
            else: 
                npc.estatos = 2 
                print(Fore.RED + '\nVocê foi derrotado ou forçado a recuar. O vilão segue seu caminho.' + Fore.RESET)
            
            Util.continuar()
            
        else: 
            self.dialogo_heroi_npc(dialogo_confronto_edran if npc.nome == 'Edran' else dialogo_confronto_kael)
            
            while True:
                Util.limpar_tela()
                print(Fore.YELLOW + f"Seu nível de Bondade é {self.heroi.bondade}. Você pode escolher o destino de {npc.nome}:" + Fore.RESET)
                Util.separacao_cabecalho()
                print("1 - Lutar contra ele. O destino do reino não pode esperar (INICIA COMBATE)")
                print("2 - Deixar que siga seu caminho. Concentre-se no Castelo Sombrio (NPC SOBREVIVE/ALIADO)")
                Util.separacao_cabecalho()
                try:
                    escolha = int(input('\nSua decisão: '))
                    if escolha == 1:
                        print(Fore.RED + f'\nVocê escolheu lutar contra {npc.nome}!' + Fore.RESET)
                        Util.pausa(2)
                        
                        self.heroi.vida = self.heroi.vidabase
                        npc.vida = npc.vidabase
                        
                        combate = Combate(self.heroi, npc)
                        combate.combate_pratico()

                        if npc.vida <= 0: 
                            npc.estatos = 2
                            print(Fore.GREEN + f'\n{npc.nome} foi derrotado. Você segue seu caminho.' + Fore.RESET)
                        else: 
                            npc.estatos = 1
                            print(Fore.RED + '\nVocê foi derrotado ou forçado a recuar. O NPC segue seu caminho.' + Fore.RESET)
                        Util.continuar()
                        return
                        
                    elif escolha == 2:
                        print(Fore.GREEN + f'\nVocê decide que {npc.nome} não é seu inimigo agora. Você segue seu caminho.' + Fore.RESET)
                        Util.pausa(2)
                        npc.estatos = 1
                        return
                    else:
                        print(Fore.RED + 'Opção inválida. Tente novamente.' + Fore.RESET)
                        Util.pausa(2)
                except ValueError:
                    print(Fore.RED + 'Entrada inválida. Digite 1 ou 2.' + Fore.RESET)
                    Util.pausa(2)

    def escolha_caminho(self):
        Util.limpar_tela()
        print('Herói, selecione, dentre as duas opções disponíveis, qual percurso deseja traçar:')
        Util.separacao_cabecalho()
        print('1 - Floresta de Auren --> Estrada de Kareth --> Castelo Sombrio')
        print('2 - Estrada de Kareth --> Floresta de Auren --> Castelo Sombrio')
        Util.separacao_cabecalho()
        try:
            escolha = int(input('Insira o caminho pelo qual deseja prosseguir: '))
        except ValueError:
            escolha = 0
            
        if escolha == 1:
            self.dialogo_heroi_npc(caminho1[0]['caminho1_floresta'])
            self.decisao_edran()
            self.aplicar_consequencia_individual(self.edran)
            
            self.dialogo_heroi_npc(caminho1[1]['caminho1_estrada'])
            self.decisao_kael()
            self.aplicar_consequencia_individual(self.kael)
            
        elif escolha == 2:
            self.dialogo_heroi_npc(caminho2[0]['caminho2_estrada'])
            self.decisao_kael()
            self.aplicar_consequencia_individual(self.kael)
            
            self.dialogo_heroi_npc(caminho2[1]['caminho2_floresta'])
            self.decisao_edran()
            self.aplicar_consequencia_individual(self.edran)
            
        else:
            print('Você selecionou uma rota inexistente!')
            Util.pausa(2)
            return