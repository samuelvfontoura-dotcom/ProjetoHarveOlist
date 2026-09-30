Projeto final do curso de Análise de Dados Harve/Florianópolis

Análise de Vendas e Logística — Olist

Análise de dados de vendas da empresa Olist entre janeiro e agosto de 2018, investigando a queda de vendas observada a partir de maio e sua relação com o custo de frete e a concentração geográfica dos vendedores. O projeto inclui um relatório analítico e um painel interativo.

Resumo do Projeto

Entre maio e julho de 2018, a Olist registrou queda nas vendas. A análise identificou que, no mesmo período, o percentual de frete sobre o valor do produto subiu de forma consistente em diversos estados (SP, RJ, MS, RS, PR, DF e GO).

Investigando a causa raiz, o estudo aponta que o problema não é apenas o aumento do frete isoladamente, mas uma fragilidade estrutural: a grande maioria dos vendedores está concentrada em São Paulo, obrigando a maior parte das entregas do país a depender de transporte de longa distância. Isso encarece o frete fora de SP, aumenta o tempo de entrega, reduz a satisfação dos clientes e, por consequência, derruba as vendas.

Perguntas de Negócio

O projeto foi guiado por quatro perguntas centrais:

Por que as vendas estão caindo?
Quem são os melhores clientes da Olist?
Problemas na entrega estão prejudicando a satisfação e as vendas?
Quais categorias de produto mais sustentam (ou derrubam) a receita?
Painel Interativo

O arquivo PROJETOHARVE.pbix é um dashboard com 5 páginas:

Visão Geral— vendas por mês, por estado, por forma de pagamento e variação mês a mês.
<img width="1526" height="846" alt="image" src="https://github.com/user-attachments/assets/36da9f27-71df-4e00-9ba1-9a0b79d434ba" />


Categorias — receita e volume por categoria, evolução mensal das top 5 categorias e nota média por faixa de atraso.
<img width="1508" height="849" alt="image" src="https://github.com/user-attachments/assets/4ad33409-1f02-452c-8cab-2524a292bab5" />


Satisfação — atraso x nota média ao longo do tempo, pedidos por faixa de valor e nota média por estado.
<img width="1496" height="847" alt="image" src="https://github.com/user-attachments/assets/cfba7f2a-e21b-4731-8174-b83761257516" />


Frete & Vendedores — frete % por estado, vendedores por estado, evolução mensal do frete nos maiores estados e comparativo SP x resto do Brasil.
Todas as páginas possuem filtros por status do pedido, estado do cliente e período.
<img width="1507" height="847" alt="image" src="https://github.com/user-attachments/assets/63bcef9a-b678-420c-a8ca-3383ee81c38d" />

SP - mostrando variação do frete e da receita da região de São Paulo
<img width="1524" height="851" alt="image" src="https://github.com/user-attachments/assets/eefc3457-903e-49b3-9d21-627f644b0373" />



Ferramentas Utilizadas

Análise exploratória e construção de indicadores

Python para tratamento dos dados

Power BI 

Base de dados pública do e-commerce Olist (jan–ago/2018)

Período analisado: janeiro a agosto de 2018.
