# League Data Crawler

Esse projeto de ciência de dados visa tentar acertar o resultado final de uma partida de League of Legends.

Esse projeto consiste de 3 arquivos principais:

1. datacrawler.ipynb: 

Após inserir o nome de um jogador, esse script de WebScraping, coleta dados das últimas 10 partidas daquele jogador, utilizando o Selenium como ferramenta. Quando a última partida é analisada,
se é selecionado aleatoriamente um dentre os 10 jogadores, para se repetir o processo em uma quantia de vezes definida no inicio do script. Este script foi utilizado para criar o conjunto de dados utilizado
para treinar o modelo.

2. modeltest.ipynb

Esse algoritmo serve para testar a precisão do modelo, para que assim se possa fazer os ajustes corretos. O modelo atual é uma amostra de 100 partidas coletadas com datacrawler.

3. mainprogram.ipynb

Esse algoritmo é o produto final, utilizando novamente o Selenium, dado um jogador que esteja em partida, ele coleta os dados dos jogadores em partida e utiliza o modelo treinado anteriormente para dar a chance de vitoria do time azul e vermelho
