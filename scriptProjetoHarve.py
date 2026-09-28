import pandas as pd

##LIMPEZA GEOLICATION 
##Carregar e analisar arquivo bruto

df = pd.read_csv('olist_geolocation_dataset.csv')
print(len(df))
df.head()
df.columns
df.dtypes

#Tirar espaços em branco no inicio/fim dos textos

df['geolocation_city'] = df['geolocation_city'].str.strip()
df['geolocation_state'] = df['geolocation_state'].str.strip()

#Padronizar o zero a esquerda do CEP
df['geolocation_zip_code_prefix'] = (df['geolocation_zip_code_prefix'].astype(str).str.zfill(5))

#Garantir que latitude e longitude são numeros
# erros='coerce' transforma qualquer valor inválido em NaN(nulo)

df['geolocation_lat'] = pd.to_numeric(df['geolocation_lat'], errors='coerce')
df['geolocation_lng'] = pd.to_numeric(df['geolocation_lng'], errors='coerce')

## Remover linhas 100% duplicadas

df = df.drop_duplicates() 
print('linhas depois da limpeza:', len(df))

# Salvar o resultado tratado em um novo arquivo CSV
df.to_csv("geolocation_tratado.csv", index=False)
print('Arquivo salvo:geolocation_tratado.csv')
df.head()





##LIMPEZA CUSTOMER
#carregar e analisar arquivo bruto 
df = pd.read_csv('olist_order_customer_dataset.csv')
df.head()
df.dtypes
df.columns
df.isnull().sum()

#Tirar espaços em branco no inicio/fim dos textos
df['customer_city'] = df['customer_city'].str.strip()
df['customer_state'] = df['customer_state'].str.strip()

#Padronizar cidade e estado em maiusculo
df['customer_city'] = df['customer_city'].str.upper()
df['customer_state'] = df['customer_state'].str.upper()

#Recuperar o zero a esquerda do CEP
df['customer_zip_code_prefix'] = (df['customer_zip_code_prefix'].astype(str).str.zfill(5))

#Remover linhas sem cidade ou sem estado
df = df.dropna(subset=['customer_city', 'customer_state'])
df = df[df['customer_state'] != ""]

#Remover linhas 100% duplicadas
df = df.drop_duplicates()

#Checar se o customer_id se repete(ele deve ser único)
duplicados = df['customer_id'].duplicated().sum()
print('customer_id duplicados encontrados:', duplicados)

print(len(df))

#Salvar o resultado tratado em um novo arquivo CSV
df.to_csv('customer_tratado.csv', index=False)
print('Arquivo salvo: customer_tratado.csv')

df.head()




##LIMPEZA ITEMS
#Carregar e analisar arquivo bruto
df = pd.read_csv('olist_order_items_dataset.csv')
print(len(df))
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco do inicio/fim dos codigos(ids)
for col in['order_id', 'product_id', 'seller_id']:
    df[col] = df[col].str.strip()

#garantir que preço e frete são numeros
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['freight_value'] = pd.to_numeric(df['freight_value'], errors='coerce')

# Garantir que a data limite de envio é uma data de verdade
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'], errors='coerce')

# Remover linhas sem preço, sem frete ou sem data valida
df=df.dropna(subset=['price', 'freight_value', 'shipping_limit_date'])

# Remover preços ou fretes negativos(não fazem sentido no mundo real)
df = df[(df['price'] >=0) & (df['freight_value']>=0)]

#Remover linhas 100% duplicadas
df = df.drop_duplicates()
print(len(df))

#Salvar o resultado tratado em um novo arquivo CSV
df.to_csv('order_items_tratado.csv', index=False)
df.head()






##LIMPEZA PAYMENTS
#Carregar e analisar dados brutos
df = pd.read_csv('olist_order_payments_dataset.csv')
len(df)
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco e padronizar o texto de payment_type
df['order_id'] = df['order_id'].str.strip()
df['payment_type'] = df['payment_type'].str.strip().str.lower()

#Garantir que as colunas numéricas são realmente numeros
df['payment_sequential'] = pd.to_numeric(df['payment_sequential'],errors='coerce')
df['payment_installments'] = pd.to_numeric(df['payment_installments'],errors='coerce')
df['payment_value'] = pd.to_numeric(df['payment_value'], errors='coerce')

#Checar problemas ANTES de decidir remover qualquer coisa
print("Valores numéricos que viraram nulos:",
      df[["payment_sequential", "payment_installments", "payment_value"]].isna().any(axis=1).sum())
print("payment_value negativo (erro real, deve ser removido):",
      (df["payment_value"] < 0).sum())
print("payment_value == 0 (válido, ex: pago 100% com voucher):",
      (df["payment_value"] == 0).sum())
print("payment_type 'not_defined' (categoria válida do dataset, não é erro):",
      (df["payment_type"] == "not_defined").sum())

#Remover SOMENTE o que é comprovadamente invalido:
# - linhas onde algum numero nao pôde ser convertido(viraria nulo)
#-valores de pagamento negativo(não existem no mundo real)
df = df.dropna(subset=['payment_sequential', 'payment_installments','payment_value' ])
df = df[df['payment_value'] >= 0]

#Remover linhas 100% duplicadas
df = df.drop_duplicates()
print(len(df))

#Salvar resultado tratado em um novo CSV
df.to_csv('payments_tratado.csv', index=False)
df.head()






##LIMPEZA REVIEWS
#Carregar e analisar o arquivo bruto

df = pd.read_csv('olist_order_reviews_dataset.csv')
len(df)
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco dos textos
df['review_comment_title'] = df['review_comment_title'].str.strip()
df['review_comment_message'] = df['review_comment_message'].str.strip()

#Garantir que as datas são datas
df['review_creation_date'] = pd.to_datetime(df['review_creation_date'], errors='coerce')
df['review_answer_timestamp'] = pd.to_datetime(df['review_answer_timestamp'], errors='coerce')

#Garantir que review_score é numero entre 1 e 5
df['review_score'] = pd.to_numeric(df['review_score'], errors='coerce')

#Checar problemas ANTES de decidir remover qualquer coisa
print('review_score invalido ou fora de 1-5:',
      (~df['review_score'].between(1, 5)).sum())

print('datas que nao converteram:',
      df[['review_creation_date', 'review_answer_timestamp']].isna().any(axis=1).sum())

print('comentarios vazios(NÃO SERA REMOVIDO):',
      df['review_comment_message'].isna().sum())

#Remover SOMENTE o que é comprovadamente invalido:
# - review_score fora do intervalo 1-5 ou que não converteu
# - datas que não converteram
# Repare que não filtrei por comentario vazio - isso é dado legitimo.
df = df.dropna(subset=['review_score', 'review_creation_date', 'review_answer_timestamp'])
df = df[df['review_score'].between(1, 5)]

#Remover apenas linhas 100% duplicadas em TODAS as colunas
#(nao usei review_id/order_id sozinhos, pois um review pode 
#legitimamente se repetir para mais de um pedido no Olist)

antes_dup = len(df)
df = df.drop_duplicates()
print('linhas removiras por serem 100% duplicadas:', antes_dup - len(df))
#apenas 4

#Salvar o resultado tratado em um novo CSV
df.to_csv('reviews_tratado.csv', index=False)
df.head()







#LIMPEZA ORDERS
#Carregar e analisar o arquivo bruto
df = pd.read_csv('olist_orders_dataset.csv')
len(df)
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco e padronizar o texto
df["order_id"] = df["order_id"].str.strip()
df["customer_id"] = df["customer_id"].str.strip()
df["order_status"] = df["order_status"].str.strip().str.lower()

#Converter todas as colunas de data para data de verdade

colunas_data = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_estimated_delivery_date'
]
for col in colunas_data:
    df[col] = pd.to_datetime(df[col], errors='coerce')


#IMPORTANTE: não removi linhas com datas vazias em order_approved_at,
#order_delivered_carrier_date ou order_delivered_customer_date.
#pedidos cancelados, em processamento ou ainda nao entregues NÃO TEM
# essas datas por natureza - isso não é erro nos dados.

#Só garanti que o essencial nunca está vazio: id do pedido, id do cliente
# e a data da compra(sem isso, a linha nao serve pra nada)

df = df.dropna(subset=['order_id', 'customer_id', 'order_purchase_timestamp'])

# Sinalizar(sem apagar) uma inconsistencia real: pedido marcado como
# 'delivered' mas sem data de entrega ao cliente registrada

inconsistentes = (df['order_status'] =='delivered') & (df['order_delivered_customer_date'].isna())
print('Pedidos "delivered" sem data de entrega(mantidos, mas revisar depois):', inconsistentes.sum())
#8 

#Remover apenas linhas 100% duplicadas
antes_dup = len(df)
df = df.drop_duplicates()
print('Linhas removidas por serem 100% duplicadas:', antes_dup - len(df))
# 0

print('linhas depois da limpeza', len(df))

#salvar o csv tratado em um novo arquivo
df.to_csv('orders_tratado.csv', index=False)






##LIMPEZA PRODUCTS
#Carregar e analisar arquivo bruto

df = pd.read_csv('olist_products_dataset.csv')
len(df)
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco do nome da categoria
df['product_category_name'] = df['product_category_name'].str.strip()

#garantir que as colunas numericas sao realmente numeros
colunas_numericas = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm",
]
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#Diagnostico ANTES de mexer em qualquer coisa
print('produtos sem categoria cadastrada(serão mantidos):',
      df['product_category_name'].isna().sum())
#610

print('Produtos com peso igual a 0(fisicamente impossivel):',
      (df['product_weight_g'] ==0).sum())
#4

#Corrigir só o que é logicamente impossivel: peso 0
# Virar nulo APENAS esse valor, sem apagar a linha do produto inteiro
# (o product_id continua existindo e é usado em outras tabelas)
df.loc[df['product_weight_g'] == 0, 'product_weight_g'] = pd.NA

# Remover apenas linhas 100% duplicadas
antes_dup = len(df) 
df = df.drop_duplicates()
print('Linhas removidas por serem inteiramente duplicadas:', antes_dup - len(df))

print('linhas depois da limpeza:', len(df))

# salvar o arquivo tratado em CSV
df.to_csv('products_tratado.csv',index=False)







##LIMPEZA SELLERS
##Carregar e analisar arquivo bruto
df = pd.read_csv('olist_sellers_dataset.csv')
len(df)
df.head()
df.dtypes
df.isnull().sum()

#Tirar espaços em branco no inicio/fim dos textos
df['seller_city'] = df['seller_city'].str.strip()
df['seller_state'] = df['seller_state'].str.strip()

#Padronizar cidade e estado em maiúsculo
df['seller_city'] = df['seller_city'].str.upper()
df['seller_state'] = df['seller_state'].str.upper()

#Recuperar o zero a esquerda do CEP
df['seller_zip_code_prefix'] = (df['seller_zip_code_prefix'].astype(str).str.zfill(5))

#Diagnostico ANTES de remover qualquer coisa
print('seller_id vazio:', df['seller_id'].isna().sum())
print('seller_id_duplicado:', df['seller_id'].duplicated().sum())
# ambos = 0

#Remover apenas linhas sem seller_id(chave usada em outras tabelas)

df = df.dropna(subset=['seller_id'])
antes_dup = len(df)
df = df.drop_duplicates()
print('linhas removidas por serem 100% duplicadas:', antes_dup - len(df))
print('linhas depois da limpeza:', len(df))

#salvar o resultado tratado em um novo arquivo CSV
df.to_csv('sellers_tratado.csv', index=False)








## Agrupamento de Clientes

#Carregar as tabelas ja tratadas
import pandas as pd
orders = pd.read_csv('orders_tratado.csv')
payments = pd.read_csv('payments_tratado.csv')
customers = pd.read_csv('customer_tratado.csv')

#Garantir que a data de compra é uma data de verdade
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

#Somar o valor pago por pedido
#Um pedido pode ter várias linhas em payments,
#por exemplo quando é pago em mais de uma forma ou em parcelas)

valor_por_pedido = payments.groupby("order_id")["payment_value"].sum().round(2).reset_index()
valor_por_pedido = valor_por_pedido.rename(columns={"payment_value": "valor_pedido"})

#Juntar pedidos + valor pago+ identificador unico do cliente
base = orders.merge(valor_por_pedido, on='order_id', how='left')
base = base.merge(customers[['customer_id', 'customer_unique_id']], on='customer_id', how='left')

#Agrupar por customer_unique_id 

clientes = base.groupby('customer_unique_id').agg(
    quantidade_pedidos=('order_id', 'count'),
    valor_total=('valor_pedido', 'sum'),
    data_primeira_compra = ('order_purchase_timestamp', 'min'),
    data_ultima_compra=('order_purchase_timestamp', 'max'),

).reset_index()

clientes['valor_total'] = clientes['valor_total'].round(2)

#Marcar clientes recorrentes(mais de 1 pedido)
clientes['status_cliente'] = clientes['quantidade_pedidos'].apply(
    lambda qtd: 'RECORRENTE' if qtd > 1 else 'NOVO'
)

print('Total de clientes unicos:', len(clientes))
print('Clientes recorrentes:', (clientes['status_cliente'] == 'RECORRENTE').sum())

#Exportar em csv
clientes.to_csv('clientes_agrupamento.csv', index=False)
