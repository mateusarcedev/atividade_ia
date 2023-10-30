import random
import time

def display(room):
    for row in room:
        print(row)

room = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P'],
]

print("Esse é o array que identifica as posições do quarto")
display(room)

x = 0
y = 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice(['Limpo', 'Sujo'])
        y += 1
    x += 1
    y = 0

print("Antes de limpar o quarto, detectei estas sujeiras aleatórias:")
display(room)

x = 0
y = 0
z = 0
cleaned_positions = []

# Capacidade máxima da bolsa e pontos de energia iniciais
capacidade_bolsa = 10
bolsa = 0
pontos_energia = 100
localizacao = 'A'
base_location = None  # Localização da base (A) para esvaziar a bolsa

# Definir uma ordem de visita a partir de 'A' até 'P'
ordem_visita = [chr(i) for i in range(ord('A'), ord('P') + 1)]
proxima_posicao = 0

while proxima_posicao < len(ordem_visita):
    posicao_atual = ordem_visita[proxima_posicao]
    
    if localizacao != posicao_atual:
        # Calcula a diferença de posição
        dx = ord(posicao_atual) - ord(localizacao)
        dy = ord(posicao_atual) - ord(localizacao)
        
        # Calcula a energia gasta para se mover na direção correta
        pontos_energia -= abs(dx) + abs(dy)

        # Atualiza a localização
        localizacao = posicao_atual

    if 0 <= x < 4 and 0 <= y < 4 and room[x][y] == 'Sujo':
        print(f"Limpando em: ({posicao_atual}, {x})")
        time.sleep(1)  # Simula o tempo para limpar
        room[x][y] = 'Limpo'
        print(f"Limpo ({posicao_atual}, {x})")
        cleaned_positions.append((posicao_atual, y))
        z += 1
        bolsa += 1
        pontos_energia -= 1  # Deduz 1 ponto de energia

        if bolsa >= capacidade_bolsa:
            print("Bolsa cheia. Voltando para a base (A) para esvaziar.")
            time.sleep(1)  # Simula o tempo para voltar à base
            print("Bolsa esvaziada.")
            bolsa = 0  # Esvazia a bolsa
            pontos_energia -= 1  # Deduz 1 ponto de energia pela viagem de retorno
            base_location = localizacao

    proxima_posicao += 1
    y += 1

    if y == 4:
        y = 0
        x += 1

# Após limpar tudo, voltar à base se necessário
if base_location:
    dx = ord(base_location) - ord(localizacao)
    dy = ord(base_location) - ord(localizacao)
    pontos_energia -= abs(dx) + abs(dy)
    localizacao = base_location
    print("Voltando à base (A) para finalizar.")
    time.sleep(1)  # Simula o tempo para voltar à base
    print("Bolsa esvaziada na base.")
    base_location = None

pro = (100 - ((z / 16) * 100))
print("Quarto está limpo agora")
display(room)
print('Performance =', pro, '%')
print('Pontos de energia usados:', 100 - pontos_energia)  # Calcula os pontos de energia usados

print("Posições Limpas:")
for position in cleaned_positions:
    print(f"({position[0]} ({position[1]})", end=', ')
print()
