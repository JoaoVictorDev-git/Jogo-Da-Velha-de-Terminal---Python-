# Jogo Da Velha Python - Terminal
Esse código permite gerar um jogo da velha, com um bot não inteligente, pois ele não pensa só sorteia numeros aleatórios

Como que funciona?
Primeiro pedimos o player e o bot, ou seja seu caractere (Ex.: 'X' e 'O');

Depois precisamos de usar de listas como:

* Posição do player -> guarda só as jogadas do jogador (humano);
* Posição do bot -> guarda só as jogadas do jogador (bot);
* Posição do jogo todo -> guarda todas as jogadas do jogador (bot) + jogador (humano);
* Lugares do jogo -> uma lista de 1 a 9, só localizar as posições de uma maneira mais facil
  
Depois pedimos para o usuario para dar um número de 1 a 9;

Calculamos se possui vaga e guadamos esse valor;

Como o jogador começa ele também termina, então logo depois calcula se o jogo acabu (9 lugares ocupado) e se alguém ganhou;

Agora roda u loop sortiando um número para o bot;

Exibimos o tabuleiro no terminal;

Verificamos a vitoria denovo.
