## Engenharia da computação, 8° Período - Noturno

## Alunos:
- Gabriel Moreira de Aguiar
- Mateus Silva Andrade Arce

##

**PEAS (Medida de Desempenho, Ambiente, Atuadores e Sensores):**

1. **Medida de Desempenho (Performance Measure):**
   - *Critério de Desempenho:* A medida de desempenho é a porcentagem de limpeza alcançada no quarto. Calculada como a proporção de posições limpas em relação ao total de posições no quarto.

2. **Ambiente (Environment):**
   - *Descrição do Ambiente:* O ambiente é representado por um quarto dividido em posições (A, B, C, ..., P), e cada posição pode estar suja ou limpa. O agente pode se mover entre as posições, limpar as posições sujas e retornar à base (A) para esvaziar a bolsa.
   - *Dinâmica do Ambiente:* O ambiente muda à medida que o agente limpa posições sujas.

3. **Atuadores (Actuators):**
   - *Ações do Agente:* Os atuadores incluem a capacidade de se mover entre as posições, limpar sujeiras e retornar à base para esvaziar a bolsa.

4. **Sensores (Sensors):**
   - *Percepções do Ambiente:* Os sensores incluem a capacidade de perceber a sujeira nas posições atuais, a localização atual do agente no ambiente e a quantidade de energia disponível.

   ##

**Implementação do PEAS no Código:**

1. **Medida de Desempenho (Performance Measure):**
   - *Critério de Desempenho:* Calculado como a porcentagem de posições limpas em relação ao total de posições no quarto. (Veja a variável `pro` no final do código)

2. **Ambiente (Environment):**
   - *Descrição do Ambiente:* O ambiente é representado pelo array `room`, onde cada posição pode estar suja ou limpa. O agente se move entre posições, limpa sujeiras e retorna à base para esvaziar a bolsa.
   - *Dinâmica do Ambiente:* O ambiente muda conforme o agente limpa posições sujas.

3. **Atuadores (Actuators):**
   - *Ações do Agente:* Os atuadores incluem a capacidade de se mover entre as posições (`x` e `y` são atualizadas), limpar sujeiras e retornar à base para esvaziar a bolsa. (Veja a parte do código relacionada à limpeza)

4. **Sensores (Sensors):**
   - *Percepções do Ambiente:* Os sensores incluem a capacidade de perceber a sujeira nas posições atuais (`room[x][y] == 'Sujo'`), a localização atual do agente (`localizacao`) e a quantidade de energia disponível (`pontos_energia`).

##

**Explicação do Código:**

1. **Geração do Ambiente:**
   - A matriz `room` é inicializada como uma representação do quarto com posições identificadas por letras de 'A' a 'P'.
   - O código preenche aleatoriamente cada posição do quarto com 'Limpo' ou 'Sujo'.

2. **Movimento e Limpeza:**
   - O agente inicia na posição (0, 0) do quarto ('A').
   - O agente segue uma ordem de visita às posições ('A' a 'P') e move-se para cada posição, limpando se a posição estiver suja.
   - A bolsa do agente tem uma capacidade máxima (`capacidade_bolsa`) e é esvaziada na base ('A') quando cheia.

3. **Cálculo de Desempenho:**
   - A medida de desempenho é calculada como a porcentagem de posições limpas no quarto.
   - Pontos de energia são deduzidos ao se mover e limpar sujeiras.

4. **Exibição de Resultados:**
   - O código exibe o estado final do quarto, a performance, os pontos de energia usados e as posições limpas.