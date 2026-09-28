Projeto final do curso de Análise de Dados Harve/Florianópolis

Análise de Vendas e Logística — Olist (2018)

Análise de dados de vendas da empresa Olist entre janeiro e agosto de 2018, investigando a queda de vendas observada a partir de maio e sua relação com o custo de frete e a concentração geográfica dos vendedores. O projeto inclui um relatório analítico e um painel interativo.

Resumo do Projeto

Entre maio e junho de 2018, a Olist registrou queda nas vendas. A análise identificou que, no mesmo período, o percentual de frete sobre o valor do produto subiu de forma consistente em diversos estados (SP, RJ, MS, RS, PR, DF e GO).

Investigando a causa raiz, o estudo aponta que o problema não é apenas o aumento do frete isoladamente, mas uma fragilidade estrutural: a grande maioria dos vendedores está concentrada em São Paulo, obrigando a maior parte das entregas do país a depender de transporte de longa distância. Isso encarece o frete fora de SP, aumenta o tempo de entrega, reduz a satisfação dos clientes e, por consequência, derruba as vendas.

Perguntas de Negócio

O projeto foi guiado por quatro perguntas centrais:

Por que as vendas estão caindo?
Quem são os melhores clientes da Olist?
Problemas na entrega estão prejudicando a satisfação e as vendas?
Quais categorias de produto mais sustentam (ou derrubam) a receita?
Painel Interativo

O arquivo painel_pbi.html é um dashboard standalone (basta abrir no navegador) com 4 páginas:

Visão Geral— vendas por mês, por estado, por forma de pagamento e variação mês a mês.
Categorias — receita e volume por categoria, evolução mensal das top 5 categorias e nota média por faixa de atraso.
Satisfação — atraso x nota média ao longo do tempo, pedidos por faixa de valor e nota média por estado.
Frete & Vendedores — frete % por estado, vendedores por estado, evolução mensal do frete nos maiores estados e comparativo SP x resto do Brasil.
Todas as páginas possuem filtros por status do pedido, estado do cliente e período.

Ferramentas Utilizadas

Análise exploratória e construção de indicadores
Power BI (relatório original) e HTML/SVG/JavaScript puro (dashboard replicado)
Base de dados pública do e-commerce Olist (jan–jul/2018)
Período analisado: janeiro a agosto de 2018.