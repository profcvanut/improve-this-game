class Personagem:
    def __init__(self, nome, vida, defesa, ataque, bondade, estatos):
        self.estatos = estatos
        self.bondade = bondade
        self.nome = nome
        self.defesa = defesa
        self.ataque = ataque
        self.vida = vida
        self.vidabase = vida
        self.ataquebase = ataque
        self.defesabase = defesa
        self.itens = [{'item': 'poção vermelha', 'qnt': 3}, 
                      {'item': 'poção azul', 'qnt': 3}, 
                      {'item': 'poção verde', 'qnt': 3}]

    def update_nome(self, nome_editado):
        
        self.nome = nome_editado
    
    def upgrade_vida(self, incremento):
        self.vida += incremento
    
    def downgrade_bondade(self, diminuir):
        self.bondade -= diminuir
        if self.bondade <= -10:
            self.bondade = -10

    def update_bondade(self, aumentar):
        self.bondade += aumentar
        if self.bondade >= 10:
            self.bondade = 10
    
    def morrer(self):
        self.estatos = 2

    def ganhar_itens(self):
        self.itens[0]['qnt'] += 2
        self.itens[1]['qnt'] += 2
        self.itens[2]['qnt'] += 2

    def __str__(self):
        return f'Personagem: {self.nome}, Vida: {self.vida}, Bondade: {self.bondade}, Itens: {self.itens}'