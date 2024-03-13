#!/usr/bin/env python
# coding: utf-8

# # Entrega Final Big Data - <span style="color:orange">**TLC NY**</span>
# ### Fabio Gerevini Canton
# ### Camila Boanova
# ### Stefani da Costa Colello

# # Introdução
# 
# ### No cenário das complexas operações urbanas, a coleta e análise de dados são fundamentais para aprimorar a eficiência e compreender os comportamentos dos indivíduos. A Taxi & Limousine Commission (TLC) em Nova York oferece uma extensa base de dados sobre as viagens realizadas na cidade, que é uma das mais movimentadas do mundo. Logo, esse trabalho se propõe a explorar e extrair insights a partir da vasta base de dados fornecida pela TLC, realizando uma análise detalhada de algumas variáveis disponíveis. O foco será identificar padrões de comportamento, fatores determinantes para o valor das viagens, duração e satisfação do cliente. Isso faz com que seja possível compreender a dinâmica das viagens e, consequentemente, otimizar as operações de uma agência de táxi fictícia.
# 
# # <span style="color:red">**Problema**</span>
# ### Diante do desafio de aprimorar a eficiência e reduzir custos tanto para os motoristas quanto para os passageiros, uma agência de táxi em Nova York busca soluções. Por isso, há uma necessidade de identificar padrões e fatores que impactam diretamente o valor das viagens, sua duração e, crucialmente, a satisfação do cliente. Nesse sentido, a análise exploratória dos dados da TLC se torna não apenas uma investigação estatística, mas uma ferramenta estratégica para a otimização das operações. Por meio dos resultados das análises, é esperado que a agência de táxi consiga implementar melhorias substanciais, maximizando a eficiência operacional e a satisfação do cliente.

# # Nessa primeira parte do código, iremos importar as bibliotecas necessárias para realizar a limpeza da base de dados e a análise dos dados.

# In[ ]:


pip install sodapy


# In[2]:


## Importando bibliotecas que serão utilizadas
import folium
import pandas as pd
from sodapy import Socrata
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os
from shapely.geometry import shape
import numpy as np


# ## Aqui, para conseguirmos comparar os diferentes anos na base de dados iremos importá-las ano a ano via API.

# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2021

client = Socrata("data.cityofnewyork.us", None)
results = client.get("m6nq-qud6", limit = 100000)

yellow_trip_2021 = pd.DataFrame.from_records(results)
yellow_trip_2021


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2020

client = Socrata("data.cityofnewyork.us", None)
results = client.get("kxp8-n2sj", limit = 100000)

yellow_trip_2020 = pd.DataFrame.from_records(results)
yellow_trip_2020


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2019

client = Socrata("data.cityofnewyork.us", None)
results = client.get("2upf-qytp", limit = 100000)

yellow_trip_2019 = pd.DataFrame.from_records(results)
yellow_trip_2019


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2018

client = Socrata("data.cityofnewyork.us",'ihlFXTVtPhq3vfO9oMm6ddpS6', timeout= 300)
results = client.get("t29m-gskq", limit = 100000)

yellow_trip_2018 = pd.DataFrame.from_records(results)
yellow_trip_2018


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2017

client = Socrata("data.cityofnewyork.us", None)
results = client.get("biws-g3hs", limit = 100000)

yellow_trip_2017 = pd.DataFrame.from_records(results)
yellow_trip_2017


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2016

client = Socrata("data.cityofnewyork.us", None)
results = client.get("uacg-pexx", limit = 100000)

yellow_trip_2016 = pd.DataFrame.from_records(results)
yellow_trip_2016


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2015

client = Socrata("data.cityofnewyork.us", None)
results = client.get("2yzn-sicd", limit = 100000)

yellow_trip_2015 = pd.DataFrame.from_records(results)
yellow_trip_2015


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2014

client = Socrata("data.cityofnewyork.us", None)
results = client.get("gkne-dk5s", limit = 100000)

yellow_trip_2014 = pd.DataFrame.from_records(results)
yellow_trip_2014


# In[ ]:


# Importando os dados pela API do NYC Open Data para o ano de 2013

client = Socrata("data.cityofnewyork.us", None)
results = client.get("t7ny-aygi", limit = 100000)

yellow_trip_2013 = pd.DataFrame.from_records(results)
yellow_trip_2013


# ## Com a base de dados importada, é necessário agora mudar o nome das colunas para concatenar os dados dos diferentes anos em um dataframe.

# In[12]:


# Mudando nome das colunas 

#2021
yellow_trip_2021 = yellow_trip_2021.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2021 = yellow_trip_2021.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2020
yellow_trip_2020 = yellow_trip_2020.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2020 = yellow_trip_2020.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2019
yellow_trip_2019 = yellow_trip_2019.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2019 = yellow_trip_2019.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2018

yellow_trip_2018 = yellow_trip_2018.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2018 = yellow_trip_2018.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2017
yellow_trip_2017 = yellow_trip_2017.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2017 = yellow_trip_2017.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2016
yellow_trip_2016 = yellow_trip_2016.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2016 = yellow_trip_2016.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})

#2015
yellow_trip_2015 = yellow_trip_2015.rename(columns={'vendor_id': 'vendorid'})
yellow_trip_2015 = yellow_trip_2015.rename(columns={'imp_surcharge': 'improvement_surcharge'})

#2014
yellow_trip_2014 = yellow_trip_2014.rename(columns={'vendor_id': 'vendorid'})
yellow_trip_2014 = yellow_trip_2014.rename(columns={'rate_code': 'ratecodeid'})
yellow_trip_2014 = yellow_trip_2014.rename(columns={'imp_surcharge': 'improvement_surcharge'})

#2013
yellow_trip_2013 = yellow_trip_2013.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
yellow_trip_2013 = yellow_trip_2013.rename(columns={'tpep_dropoff_datetime': 'dropoff_datetime'})


# In[ ]:


# Concatenando os dados de todos os anos importados

yellow_trip_21_13 = pd.concat([yellow_trip_2021,
                                yellow_trip_2020,
                                yellow_trip_2019,
                                yellow_trip_2018,
                                yellow_trip_2017,
                                yellow_trip_2016,
                                yellow_trip_2015,
                                yellow_trip_2014,
                                yellow_trip_2013])
yellow_trip_21_13


# ## Dado que estamos trabalhando com uma base de dados bem extensa e tendo em vista o nosso problema escolhido, não será necessário utilizar todas as colunas e dados oferecidos pelo TLC. Assim, na parte seguinte do código iremos filtrar apenas as variáveis que queremos analisar e interpretar.

# In[ ]:


# Selecionando variaveis a serem usadas na analise

yellow_trip_21_13 = yellow_trip_21_13.loc[:,['pickup_datetime',
                                      'dropoff_datetime',
                                      'trip_distance',
                                      'passenger_count',
                                      'pulocationid',
                                      'dolocationid',
                                      'ratecodeid',
                                      'store_and_fwd_flag',
                                      'fare_amount',
                                      'extra',
                                      'tolls_amount',
                                      'congestion_surcharge',
                                      'pickup_longitude',
                                      'pickup_latitude',
                                      'dropoff_longitude',
                                      'dropoff_latitude',
                                      'pickup_location',
                                      'dropoff_location',
                                      'payment_type'
                                      ]]

yellow_trip_21_13['dropoff_datetime'] = pd.to_datetime(yellow_trip_21_13['dropoff_datetime'])
yellow_trip_21_13['pickup_datetime'] = pd.to_datetime(yellow_trip_21_13['pickup_datetime'])
yellow_trip_21_13['trip_duration'] = yellow_trip_21_13['dropoff_datetime'] - yellow_trip_21_13['pickup_datetime']
yellow_trip_21_13


# ## Em primeiro lugar na análise, buscamos entender em quais regiões de NY há mais demanda por táxis. Para isso, iremos gerar um mapa de calor para a visualização das zonas (e de suas respectivas quantidades) dos pontos de partida das corridas.

# In[15]:


lat_long_pick = yellow_trip_21_13[['pickup_longitude','pickup_latitude']]
lat_long_limpo_pick = lat_long_pick.dropna(subset=['pickup_longitude','pickup_latitude'])
lat_long_limpo_pick


# In[16]:


lat_list_pick = lat_long_limpo_pick["pickup_latitude"].to_list()
lng_list_pick = lat_long_limpo_pick["pickup_longitude"].to_list()


# In[17]:


# Mapa de calor
mapa = folium.Map(
    location=[28.5856559, -80.6507658],
    zoom_start=4
)

HeatMap(list(zip(lat_list_pick, lng_list_pick))).add_to(mapa)

mapa


# ## Em segundo lugar na análise, buscamos entender para quais regiões de NY esses indivíduos mais têm como destino. Para isso, iremos fazer outro mapa de calor, dessa vez com os pontos de chegada das corridas.

# In[18]:


lat_long_drop = yellow_trip_21_13[['dropoff_longitude','dropoff_latitude']]
lat_long_limpo_drop = lat_long_drop.dropna(subset=['dropoff_longitude','dropoff_latitude'])
lat_long_limpo_drop = lat_long_limpo_drop.T.drop_duplicates().T
lat_long_limpo_drop


# In[19]:


lat_list_drop = lat_long_limpo_drop["dropoff_latitude"].to_list()
lng_list_drop = lat_long_limpo_drop["dropoff_longitude"].to_list()


# In[50]:


# Mapa de calor
mapa = folium.Map(
    location=[28.5856559, -80.6507658],
    zoom_start=4
)

HeatMap(list(zip(lat_list_drop, lng_list_drop))).add_to(mapa)

mapa


# ## Para visualizar melhor as informações que buscamos, plotaremos um gráfico da demanda por hora do dia. Dessa forma, conseguiremos achar em qual hora do dia ocorre o maior número de pickups e dropoffs.

# In[21]:


# Contagem por semana de pickup_datetime

yellow_trip_21_13['pickup_datetime'] = pd.to_datetime(yellow_trip_21_13['pickup_datetime'])
yellow_trip_21_13['week_of_year'] = yellow_trip_21_13['pickup_datetime'].dt.isocalendar().week
weekly_counts = yellow_trip_21_13.groupby('week_of_year').size()


# In[22]:


# Demanda de taxis por hora do dia para todos os anos
# Conversão de datas
yellow_trip_21_13['pickup_datetime'] = pd.to_datetime(yellow_trip_21_13['pickup_datetime'])
yellow_trip_21_13['dropoff_datetime'] = pd.to_datetime(yellow_trip_21_13['dropoff_datetime'])

# Extração de informações temporais
yellow_trip_21_13['pickup_hour'] = yellow_trip_21_13['pickup_datetime'].dt.hour
yellow_trip_21_13['pickup_dayofweek'] = yellow_trip_21_13['pickup_datetime'].dt.dayofweek
yellow_trip_21_13['pickup_month'] = yellow_trip_21_13['pickup_datetime'].dt.month

# Análise de demanda por hora
hourly_demand = yellow_trip_21_13.groupby('pickup_hour').size()
hourly_demand.plot(kind='bar')
plt.title('Demanda por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Viagens')
plt.show()


# ### Analisando o gráfico acima e considerando as corridas de um período de 2013 até 2021, é possível inferir que os horários de maior demanda são entre 10h - 13h, assim como das 17h - 19h. Esse resultado era esperado, dado que abrange horários movimentados de chegada e saída do trabalho e também horário do almoço. Outro dado esperado era de que as corridas no período da madrugada tivessem menor demanda.

# ## Agora, plotaremos um gráfico da demanda por mês para que seja possível identificas em qual mês ocorre o maior número de pickups e dropoffs.

# In[23]:


# Conversão de datas
yellow_trip_21_13['pickup_datetime'] = pd.to_datetime(yellow_trip_21_13['pickup_datetime'])
yellow_trip_21_13['dropoff_datetime'] = pd.to_datetime(yellow_trip_21_13['dropoff_datetime'])

# Extração de informações temporais
yellow_trip_21_13['pickup_hour'] = yellow_trip_21_13['pickup_datetime'].dt.hour
yellow_trip_21_13['pickup_dayofweek'] = yellow_trip_21_13['pickup_datetime'].dt.dayofweek
yellow_trip_21_13['pickup_month'] = yellow_trip_21_13['pickup_datetime'].dt.month

# Análise de demanda por hora
hourly_demand = yellow_trip_21_13.groupby('pickup_month').size()
hourly_demand.plot(kind='bar')
plt.title('Demanda por mês')
plt.xlabel('Mês do Ano')
plt.ylabel('Número de Viagens')
plt.show()


# ## O gráfico mostra a demanda mensal anual de táxis em Nova York, com picos notáveis nos meses de janeiro (1), março (3), junho (6) e dezembro (12). Algumas possíveis explicações:
# 
# ### 1. Janeiro: Este pico pode ser devido ao turismo de inverno e ao grande número de pessoas que retornam de viagens de férias após o Ano Novo. Além disso, janeiro é marcado por liquidações pós-férias e eventos especiais que podem aumentar a demanda por táxis.
# ### 2. Março: Eventos Especiais: Março abriga eventos como o Desfile do Dia de São Patrício, que é uma grande celebração na cidade e atrai muitos visitantes, Clima: transição do inverno para a primavera pode trazer dias mais quentes, incentivando as pessoas a saírem mais e usarem táxis para se deslocarem e Férias de Primavera: Universidades e escolas muitas vezes têm suas férias de primavera em março, o que pode resultar em mais viagens locais e turismo familiar.
# ### 3. Junho: O aumento no mês de junho pode ser atribuído à temporada de verão, quando o turismo está em alta. Eventos como a Parada do Orgulho LGBTQ+, festivais e conferências, bem como o término do ano letivo, podem levar a um aumento na demanda por transporte.
# 
# ### 4. Dezembro: O pico em dezembro é provavelmente devido às festividades de fim de ano, como o Natal e a véspera de Ano Novo, que atraem muitos turistas e provocam um aumento nas atividades sociais. As condições climáticas de inverno também podem fazer com que mais pessoas optem por táxis em vez de transporte público ou caminhadas.
# 
# ## A sazonalidade também pode ser afetada por fatores como condições climáticas adversas, que podem aumentar a demanda por táxis em meses com tempo mais severo, e feriados, que podem tanto aumentar a demanda por lazer quanto afetar a oferta de motoristas disponíveis.

# In[ ]:


# Extração de informações temporais
yellow_trip_21_13['pickup_hour'] = yellow_trip_21_13['pickup_datetime'].dt.hour
yellow_trip_21_13['pickup_dayofweek'] = yellow_trip_21_13['pickup_datetime'].dt.dayofweek
yellow_trip_21_13['pickup_month'] = yellow_trip_21_13['pickup_datetime'].dt.month

yellow_trip_21_13


# ## Depois de analizar os horários e meses com maior movimento de viagens de táxi, realizaremos uma matriz de correlação das variáveis escolhidas pelo grupo para analisar.

# In[25]:


# correlação entre preço da tarifa e distancia de viagem

yellow_trip_21_13['fare_amount'] = yellow_trip_21_13['fare_amount'].astype(float)
yellow_trip_21_13['trip_distance'] = yellow_trip_21_13['trip_distance'].astype(float)

fare_trip = yellow_trip_21_13[(yellow_trip_21_13 ['fare_amount'] > 0) & (yellow_trip_21_13 ['trip_distance'] > 0)]

correlation = fare_trip['fare_amount'].corr(fare_trip['trip_distance'])
print(f"Correlação entre Tarifa e Distância da Viagem: {correlation}")


# In[26]:


correlation_table = yellow_trip_21_13.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_table, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()


# ## O que podemos concluir dessa matriz de correlação é que:
# 
# ### Existe uma forte correlação positiva entre a semana do ano em que ocorre o pickup e o dia da semana desse mesmo pickup. Há também uma correlação positiva entre a hora do pickup com o mês desse mesmo pickup. Enquanto a primeira não tem explicações muito diretas, a segunda correlação pode ser relacionado com as estações. No inverno, quando os dias são mais curtos, as horas de pico de pickups podem ser mais tarde, durante as horas mais escuras do dia, levando a diferentes padrões de pickups.
# 
# ### Por outro lado, há uma forte correlação negativa entre o dia da semana do pickup e o respectivo mês desse mesmo pickup. Por exemplo, se observarmos pickups que ocorrem aos sábados, podemos notar que eles tendem a se distribuir ao longo de vários meses, não se concentrando exclusivamente em um único mês. Além disso, também há uma correlação negativa entre a hora do pickup com o dia da semana desse pickup. Nesse caso, as análises dos pickups durante a madrugada, por exemplo, podem estar distribuídas de forma diferente ao longo dos dias da semana já que essa hora específica não é exclusiva de um dia particular da semana.
# 
# ### As outras correlações são muito baixas e provavelmente não tem conexão. No entanto, não podemos desconsiderar as relações entre essas mesmas variáveis.

# ## O objetivo da análise agora é descobrir quais são os top 10 locais (local ID) de pickup e dropoff, derivado da frequência em que determinada zona aparece na base de dados entre 2013 e 2021.

# In[27]:


# Contagem de locais de pickup mais comuns
locais_coleta_count = yellow_trip_21_13['pulocationid'].value_counts()

# Contagem de locais de dropoff mais comuns
locais_entrega_count = yellow_trip_21_13['dolocationid'].value_counts()

# Soma das contagens de pickup e dropoff para identificar áreas de alta demanda
total_locais_count = locais_coleta_count.add(locais_entrega_count, fill_value=0)

# Classifique os locais pelo total de ocorrências em ordem decrescente
locais_mais_comuns = total_locais_count.sort_values(ascending=False)

# Visualize os 10 locais mais comuns
top_10_locais = locais_mais_comuns.head(10)

# Crie um gráfico de barras para visualizar os locais mais comuns
plt.figure(figsize=(10, 6))
top_10_locais.plot(kind='bar', color='skyblue')
plt.title('Top 10 Locais de Pickup/Dropoff Mais Comuns')
plt.xlabel('Local ID')
plt.ylabel('Contagem')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 

# ## Para complementar a nossa análise, construiremos alguns gráficos do comportamento de variáveis que consideramos de extrema importância para a efeciência da agência de táxi. As variáveis escolhidas são as seguintes:

# In[28]:


yellow_trip_21_13['trip_duration'] = pd.to_timedelta(yellow_trip_21_13['trip_duration'])
yellow_trip_21_13['trip_duration'] = yellow_trip_21_13['trip_duration'].dt.total_seconds() / 60

# Agregando dados por hora do dia
hourly_stats = yellow_trip_21_13.groupby('pickup_hour').agg({
    'fare_amount': 'mean',       # Valor médio da corrida
    'trip_duration': 'mean'      # Duração média da corrida
}).reset_index()

# Agregando dados por dia da semana
daily_stats = yellow_trip_21_13.groupby('pickup_dayofweek').agg({
    'fare_amount': 'mean',
    'trip_duration': 'mean'
}).reset_index()

# Agregando dados por mês
monthly_stats = yellow_trip_21_13.groupby('pickup_month').agg({
    'fare_amount': 'mean',
    'trip_duration': 'mean'
}).reset_index()

# Gráficos para a análise por hora do dia
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
plt.bar(hourly_stats['pickup_hour'], hourly_stats['fare_amount'])
plt.title('Valor Médio da Corrida por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Valor Médio ($)')

plt.subplot(1, 3, 2)
plt.bar(daily_stats['pickup_dayofweek'], daily_stats['fare_amount'])
plt.title('Valor Médio da Corrida por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor Médio ($)')
plt.xticks(range(7), ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'])

plt.subplot(1, 3, 3)
plt.bar(monthly_stats['pickup_month'], monthly_stats['fare_amount'])
plt.title('Valor Médio da Corrida por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor Médio ($)')

plt.tight_layout()
plt.show()

# Gráficos para a análise de duração por hora do dia
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
plt.bar(hourly_stats['pickup_hour'], hourly_stats['trip_duration'])
plt.title('Duração Média da Corrida por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Duração Média (min)')

plt.subplot(1, 3, 2)
plt.bar(daily_stats['pickup_dayofweek'], daily_stats['trip_duration'])
plt.title('Duração Média da Corrida por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Duração Média (min)')
plt.xticks(range(7), ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'])

plt.subplot(1, 3, 3)
plt.bar(monthly_stats['pickup_month'], monthly_stats['trip_duration'])
plt.title('Duração Média da Corrida por Mês')
plt.xlabel('Mês')
plt.ylabel('Duração Média (min)')

plt.tight_layout()
plt.show()



# ### <span style="color:blue">**VALOR**</span>: O valor médio da corrida por hora se mantém constante na maior parte do dia, mas é possível inferir que entre 4h - 5h e as 9h possuem valores mais altos - seja pela disponibilidade menor de táxis na madrugada ou pelo horário de pico de entrada no trabalho. Já o valor médio da corrida por dia da semana, é possível dizer que os valores de sexta e domingo são mais altos, que seria o início e fim do final de semana. Quanto aos valores por mês, os dados indicam que o valor médio em Março é o maior de todos, mas não há explicação visível para isso. 
# 
# ### <span style="color:purple">**Duração**</span>: A duração média da corrida por hora tende a ser maior na madrugada entre 00h - 4h e 15h - 16h. Isso é contraditório dado que era esperado que os horários de pico de entrada e saída do trabalho causasse aumento da duração da corrida e, ao mesmo tempo, que corridas na madrugada fossem mais rápidas por conta do baixo fluxo de tráfego nesse período. Já a duração média da corrida por dia da semana aparenta ser igual e as pequenas diferenças sem explicações aparentes nos dados. Por fim, a duração média da corrida por mês tende a ser maior entre Dezembro e Janeiro e isso pode ser explicado pelo número de turista que visitam a cidade nesses meses e, consequentemente, o aumento do tráfego de pessoas se locomovendo na cidade.

# ## Outro fator importante que queremos analisar é o impacto das sobretaxas de congestionamento na corrida de táxi e seu impacto no valor total da viagem. Essas sobretaxas podem significar um aumento substancial no custo total da viagem para o passageiro e, por isso, elas influenciam diretamente na percepção de valor do serviço de táxi. Por outro lado, as sobretaxas podem influenciar o comportamento dos motoristas de táxi, levando-os a optar por rotas alternativas.

# In[29]:


Q1 = yellow_trip_21_13['fare_amount'].quantile(0.25)
Q3 = yellow_trip_21_13['fare_amount'].quantile(0.75)
IQR = Q3 - Q1
# Ajustando o multiplicador
filtro = (yellow_trip_21_13['fare_amount'] >= Q1 - 1.5 * IQR) & (yellow_trip_21_13['fare_amount'] <= Q3 + 1.5 * IQR)
df_filtrado = yellow_trip_21_13.loc[filtro]

# Plotando o boxplot para 'fare_amount' com os dados filtrados
plt.figure(figsize=(10, 6))
sns.boxplot(x='congestion_surcharge', y='fare_amount', data=df_filtrado)

# Definindo os limites do eixo y
plt.ylim(df_filtrado['fare_amount'].min(), df_filtrado['fare_amount'].max())

plt.title('Distribuição do Valor da Viagem por Sobretaxa de Congestionamento')
plt.xlabel('Sobretaxa de Congestionamento')
plt.ylabel('Valor da Viagem (fare_amount)')
plt.show()


# ### Analisando os boxplots, é possível inferir que ao considerar uma sobretaxa de 2.5 os valores mudam substancialmente - havendo uma grande diferença entre o mínima e o máximo pagos nessa corrida. Além disso, é importante ressaltar que justo nesse valor de sobretaxa há um número enorme de outliers nos valores mais altos, indicando que efetivamente essas sobretaxas de congestionamento aumentam os valores das viagens de forma expressiva.

# ## Conferindo os tipos de dados existentes em fare amount
# - Taxas negativas (advindas de cancelamentos)
# - Taxa zero (não houve inclusão de taxa na corrida)
# - Taxas maiores que 100 dólares

# In[30]:


print(f"There are {len(yellow_trip_21_13[yellow_trip_21_13['fare_amount'] < 0])} negative fares.")
print(f"There are {len(yellow_trip_21_13[yellow_trip_21_13['fare_amount'] == 0])} $0 fares.")
print(f"There are {len(yellow_trip_21_13[yellow_trip_21_13['fare_amount'] > 100])} fares greater than $100.")


# ## Esses números indicam que muitas pessoas cancelam as corridas devido as sobretaxas de congestionamento (1.532) e que a maioria das corridas no total (2.204) sofrem aplicação dessas sobretaxas. É válido ressaltar que a implementação dessa taxa foi uma tentativa do governo de tentar diminuir os congestionamentos na cidade e diminuir a demanda em horários de pico.
# ### OBS: Essa taxa não foi muito bem aceita pelos taxistas, uma vez que ela reduziu o valor que eles recebiam

# ## Dito isso, é importante comparar a quantidade de viagens que são feitas com aplicação dessa sobretaxa de congestionamento e sem a sobretaxa.

# In[ ]:


# Criando uma coluna booleana que será True se houver sobretaxa (taxa extra para lugares específicos) e False caso contrário
yellow_trip_21_13['congestion_surcharge'] = yellow_trip_21_13['congestion_surcharge'].astype(float)
yellow_trip_21_13['has_congestion_surcharge'] = yellow_trip_21_13['congestion_surcharge'] > 0

# Contando o número de viagens com e sem sobretaxa
surcharge_counts = yellow_trip_21_13['has_congestion_surcharge'].value_counts()

# Criando o gráfico de barras
colors = ['purple', 'orange']
plt.figure(figsize=(10, 6))
plt.bar(surcharge_counts.index.map({True: 'Com Sobretaxa', False: 'Sem Sobretaxa'}), surcharge_counts.values, color = colors)
plt.title('Número de Viagens com e sem Sobretaxa de Congestionamento')
plt.ylabel('Número de Viagens')
plt.show()


# ## Conforme o esperado, há um número muito maior de viagens quando não há a imposição das sobretaxas de congestionamentos. Isso pode ser explicado de maneira bem simples. Quando há sobretaxas devido ao congestionamento, as pessoas tendem a esperar um pouco mais de tempo para pedir o táxi do que pagar mais caro para realizar a corrida naquele momento. Assim, as corridas com a aplicação desse tipo de taxa só ocorrem com aqueles que têm pressa ou não querem esperar - optando por pagar mais caro e fazer a corrida naquele momento.

# ## Agora, iremos agrupar um conjunto de valores em um número de bins para visualizar a dispersão e quantidade de ocorrências das corridas de táxi por intervalo de fares.

# In[32]:


data = yellow_trip_21_13[yellow_trip_21_13['fare_amount'].between(left = 2.5, right = 100)]


# In[33]:


data = data.copy()

# Fazendo bins para as tarifa e converter para string
data['fare-bin'] = pd.cut(data['fare_amount'], bins=list(range(0, 50, 5))).astype(str)

# Ajustar o bin mais alto
data.loc[data['fare-bin'] == 'nan', 'fare-bin'] = '[45+]'

# Ajustar o bin por ordenação 
data.loc[data['fare-bin'] == '(5, 10]', 'fare-bin'] = '(05, 10]'

# Gráfico de barras da contagem de valores
data['fare-bin'].value_counts().sort_index().plot.bar(color='b', edgecolor='k')
plt.title('Intervalo das Fares')
plt.show()


# ## Em sua grande maioria, as corridas de táxi custam em torno de 1-20 dólares, sendo o mais comum entre 5 e 10 doláres. Isso ocorre porque as corridas de táxi em NY são por natureza caras. Assim, as pessoas que costumam pegar corridas de táxi utilizam-as para ir a lugares relativamente perto e, raramente, para lugares mais longes. Isso explica o motivo da maioria das fares serem preços baixos e, ao mesmo tempo, poucas corridas serem de valores altos.

# ## Por fim, iremos importando a API do Shapefile para criar um mapa de calor mais visual para realizar a nossa análise do problema de táxis em NY proposto inicialmente.

# In[34]:


client = Socrata("data.cityofnewyork.us", None)
zones_shape = client.get("755u-8jsi")


# In[ ]:


geometries = [shape(d['the_geom']) if 'the_geom' in d else None for d in zones_shape]

# Criando df com as zonas
df = pd.DataFrame(zones_shape)
df['geometry'] = geometries

# Convertendo df em um geodf
zones_geo_df = gpd.GeoDataFrame(df, geometry='geometry')
zones_geo_df


# In[36]:


zones_shape = gpd.GeoDataFrame(zones_geo_df)


# In[ ]:


zones_shape


# In[38]:


zones_shape.objectid = pd.to_numeric(zones_shape.objectid)


# In[39]:


zones_shape.location_id = pd.to_numeric(zones_shape.location_id)


# In[ ]:


pip install matplotlib.colors


# In[41]:


from matplotlib.colors import LinearSegmentedColormap


# In[42]:


zones_shape['objectid'] = zones_shape['objectid'].astype(float)
yellow_trip_21_13['pulocationid'] = yellow_trip_21_13['pulocationid'].astype(float)


# In[ ]:


# Realizando o merge entre o dataframe yellow_trip_21_13 e zones_shape
merged_data = zones_shape.merge(yellow_trip_21_13, left_on="objectid", right_on="pulocationid")
merged_data


# In[ ]:


merged_data.info()


# In[45]:


fig, ax = plt.subplots(figsize=(12, 8))

merged_data.plot(column="pulocationid", cmap="OrRd", ax=ax)

ax.set_title("NYC Taxi Pickup Locations")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
cbar = fig.colorbar(ax.collections[0])

plt.show()


# In[46]:


soma_por_bairro = merged_data.groupby('zone')['passenger_count'].describe()
soma_por_bairro_ordenado = soma_por_bairro.sort_values(by='count', ascending = False)
soma_por_bairro_ordenado = soma_por_bairro_ordenado.reset_index()
soma_por_bairro_ordenado_top_10 = soma_por_bairro_ordenado.head(10)


# In[47]:


soma_por_bairro_ordenado_top_10


# ### A maioria das zonas tem o número mais comum de passageiros por corrida como 1, o que sugere que as corridas individuais são as mais frequentes nesses locais.
# ### As zonas listadas são provavelmente algumas das mais movimentadas em termos de serviço de táxi, considerando o alto número total de corridas registradas.
# ### A variação na contagem entre as zonas pode indicar diferenças na demanda por táxis, que pode ser influenciada por fatores como densidade populacional, proximidade a atrações turísticas ou centros de negócios, e disponibilidade de outras formas de transporte.

# In[48]:


plt.figure(figsize=(10, 8))
plt.barh(soma_por_bairro_ordenado_top_10['zone'], soma_por_bairro_ordenado_top_10['count'], color='skyblue')
plt.xlabel('count')
plt.ylabel('zone')
plt.title('Count by Zone')
plt.show()


# ## O gráfico plotado, coloca de forma visual os dados da tabela acima. Para poder interpretar algumas possíveis explicações para a ordem do Top 10: 
# ### 1. Padrão de Demanda por Zona: As barras representam a quantidade de corridas de táxi em cada zona. A "Upper East Side South" tem o maior número de corridas, o que poderia ser devido a uma alta densidade populacional, uma área comercial popular ou uma combinação de fatores que atraem um grande número de passageiros.
# ### 2. Conveniência de Localização: Zonas como "Upper East Side North" e "Midtown Center" também têm uma alta contagem, o que pode ser explicado pela presença de muitos escritórios, pontos turísticos, ou uma conexão central de transporte que faz com que essas áreas sejam destinos ou pontos de partida comuns para passageiros de táxi.
# ### 3. Impacto dos Aeroportos: O "JFK Airport" está incluído na lista, o que não é surpreendente, já que aeroportos são pontos de trânsito significativos e muitas pessoas usam táxis para se deslocar de e para lá.
# ### 4. Áreas Residenciais e Comerciais: Zonas residenciais como a "Upper West Side South" podem ter uma alta contagem devido ao padrão diário de deslocamento dos residentes. Da mesma forma, áreas com muitos restaurantes, bares e vida noturna, como o "East Village", podem gerar muitas corridas de táxi, especialmente durante as noites e fins de semana.
# ### 5. Variações Sazonais ou Eventuais: Se esses dados foram coletados durante um período específico, eventos especiais, como festivais ou conferências, poderiam temporariamente aumentar a demanda por táxis em certas zonas.
# ### 6. Preferências de Transporte: As diferenças na contagem também podem refletir as preferências de transporte locais. Algumas zonas podem ter melhor acesso ao metrô de Nova York ou a outras formas de transporte público, possivelmente reduzindo a dependência de táxis.
# ### 7. Infraestrutura e Acessibilidade: A facilidade de acesso e a disponibilidade de táxis em determinadas zonas também podem influenciar esses números. Por exemplo, se uma zona é bem servida por pontos de táxi ou tem regulamentações que facilitam as paradas de táxi, isso pode aumentar o número de corridas.

# # <span style="color:red">**Conclusão**</span>
# ### Em resumo, a análise de dados permite a obtenção de insights valiosos para a gestão de serviços da agência de táxi em NY. Inicialmente, é fundamental considerar a disponibilidade de táxis nos horários de pico (das 10h às 12h e das 16h às 18h) nas áreas com maior número de embarques e desembarques (como nas regiões identificadas pelas zonas 48, 236 e 161). Outro ponto relevante é a observação da demanda por táxis ao longo dos meses, especialmente durante os períodos mais movimentados, como janeiro, março e dezembro. Por fim, é crucial que a agência avalie com cautela a aplicação de tarifas de congestionamento. Embora a imposição dessas taxas possa parecer benéfica para os motoristas, a análise demonstra que com a sobretaxa, os condutores deixam de realizar as corridas. Essa prática de atenção com os valores da sobretaxa contribuem para a manutenção de tarifas acessíveis e atrativas aos consumidores, mantendo os valores das tarifas em patamares aceitáveis.
# 
# ### Essa análise permite à agência de táxi aprimorar sua eficiência operacional. Ao identificar os horários de pico e as áreas mais movimentadas, a distribuição dos veículos pode ser otimizada, reduzindo os tempos de espera dos passageiros e aumentando a quantidade de corridas realizadas. Isso não apenas melhora a renda dos motoristas, mas também eleva a satisfação dos consumidores, garantindo acesso mais rápido ao serviço. Além disso, ao monitorar as tarifas de congestionamento, a agência pode manter um equilíbrio entre ganhos dos condutores e atratividade para os clientes, mantendo tarifas estáveis. Esses insights não só otimizam as operações, mas também criam um ambiente mais eficiente e satisfatório para todos as partes envolvidas nos serviços de táxi.
