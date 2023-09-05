import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.ensemble import IsolationForest
# MATRIX
import os
# MATRIX

###################
# outliers,agrupamento e visualização dos dados
# Original enviado por Pâmella
# df = pd.read_csv('../discBiologia_Moodle_filled.csv',encoding = "UTF-8", sep = ";")
# MATRIX
df = pd.read_csv('../discBiologia_Moodle_filled.csv',encoding = "UTF-8", sep = ",")
# MATRIX
# print(df)
#dfMC=df[df['disciplina']=='Metodologia cientifica']
dfMC=df[df['nome_da_disciplina']=='Zoologia invertebrados']
#print(dfMC)
dfMC.fillna(0, inplace=True)
dfMC2 = dfMC.drop(dfMC.columns[[0, 1,2,3,4,5]], axis=1)
dfMC2.fillna(0, inplace=True)
#print(dfMC2)#tirando colunas categoricas para rodar o algoritmo

###################
# Outliers
#encontrado dados anomalos
model_IF = IsolationForest(contamination=float(0.1),random_state=42)
model_IF.fit(dfMC2)
dfMC2['anomaly'] = model_IF.predict(dfMC2)
dfMC['anomaly'] = dfMC2['anomaly']

#filtrando p pegar apenas nao anomalos
filtro  = dfMC2['anomaly'] == 1
filtro  = dfMC['anomaly'] == 1
#preciso de dois df's um com dados categoricos que sera usado dps p lotar
# e outro sem dados categoricos p colocar n agrupamento
dfSemOuliers = dfMC[dfMC['anomaly'] == 1]
dfSemOuliers2 =  dfMC2[dfMC2['anomaly'] == 1]

###################
# AGRUPAMENTO
# #algotimo de agrupamento c o df sem outlier e sem dados categoricos
kmeanModel = KMeans(n_clusters=2) #ja rodei o Elbow é c esse k=2 msm
kmeanModel.fit(dfSemOuliers2)
dfSemOuliers['Grupos']=kmeanModel.predict(dfSemOuliers2)
df = dfSemOuliers


#isso é so p ficar bonito na hora de plotar os graficos
df['Grupos'] = df['Grupos'].replace(1,"Grupo 1")
df['Grupos'] = df['Grupos'].replace(0,"Grupo 0")

###################
# Visualizaçao
#df para plotar
# print(df)   #sem outlier, c info dos alunos, c info dos grupos para plotar os graficos

###################
# Gráfico de área
#selecionando apenas as variaveis que serao utilizadas
grafArea = df.loc[:,[
'1semanavar079', '2semanavar079', '3semanavar079','4semanavar079',
'1semanavar0710', '2semanavar0710', '3semanavar0710','4semanavar0710',
'1semanavar0711', '2semanavar0711', '3semanavar0711','4semanavar0711',
'1semanavar0712', '2semanavar0712', '3semanavar0712','4semanavar0712','Grupos']]

#agrupando por grupos

d = grafArea.groupby(['Grupos']).sum().reset_index()

#transformando coluna em linha (apenas para fazer a plotagem)
data1 = pd.melt(d.reset_index(), id_vars='Grupos',
value_vars=[
'1semanavar079', '2semanavar079', '3semanavar079','4semanavar079',
'1semanavar0710', '2semanavar0710', '3semanavar0710','4semanavar0710',
'1semanavar0711', '2semanavar0711', '3semanavar0711','4semanavar0711',
'1semanavar0712', '2semanavar0712', '3semanavar0712','4semanavar0712'], var_name='Semanas', value_name='Quantidade')

#atualizando o nome (apenas para plotar organizado)

data1 = data1.replace('1semanavar079','1-7 Setembro')
data1 = data1.replace('2semanavar079','8-15 Setembro')
data1 = data1.replace('3semanavar079','16-24 Setembro')
data1 = data1.replace('4semanavar079','25-30 Setembro')
data1 = data1.replace('1semanavar0710','1-7 Outubro')
data1 = data1.replace('2semanavar0710','8-15 Outubro')
data1 = data1.replace('3semanavar0710','16-24 Outubro')
data1 = data1.replace('4semanavar0710','25-31 Outubro')
data1 = data1.replace('1semanavar0711','1-7 Novembro')
data1 = data1.replace('2semanavar0711','8-15 Novembro')
data1 = data1.replace('3semanavar0711','16-24 Novembro')
data1 = data1.replace('4semanavar0711','25-30 Novembro')
data1 = data1.replace('1semanavar0712','1-7 Dezembro')
data1 = data1.replace('2semanavar0712','8-15 Dezembro')
data1 = data1.replace('3semanavar0712','16-24 Dezembro')
data1 = data1.replace('4semanavar0712','25-31 Dezembro')


#dados a serem plotados
# print(data1)

#plotagem
fig = px.area(data1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

fig.update_layout(autosize=False,width=900,height=600)
fig.update_layout(title={
    'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo',
    'y':0.96,
    'x': 0.1
})
fig.update_xaxes(title = 'Períodos Mensais')
fig.update_yaxes(title = 'Quantidade Visualização')
# MATRIX
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/linhas1.png")
# MATRIX

###################
# 3) Gráfico de Linha
#selecionando apenas as variaveis que serao utilizadas
dgraflinha = df.loc[:,[
'1semanavar029', '2semanavar029', '3semanavar029','4semanavar029',
'1semanavar0210', '2semanavar0210', '3semanavar0210','4semanavar0210',
'1semanavar0211', '2semanavar0211', '3semanavar0211','4semanavar0211',
'1semanavar0212', '2semanavar0212', '3semanavar0212','4semanavar0212',
'Grupos']]

d = dgraflinha.groupby(['Grupos']).sum().reset_index()

dataR = pd.melt(d.reset_index(), id_vars='Grupos',
value_vars=[
'1semanavar029', '2semanavar029', '3semanavar029','4semanavar029',
'1semanavar0210', '2semanavar0210', '3semanavar0210','4semanavar0210',
'1semanavar0211', '2semanavar0211', '3semanavar0211','4semanavar0211',
'1semanavar0212', '2semanavar0212', '3semanavar0212','4semanavar0212'], var_name="Dias da Semana", value_name="Quantidade")


dataR = dataR.replace('1semanavar029','1-7 Setembro')
dataR = dataR.replace('2semanavar029','8-15 Setembro')
dataR = dataR.replace('3semanavar029','16-24 Setembro')
dataR = dataR.replace('4semanavar029','25-30 Setembro')
dataR = dataR.replace('1semanavar0210','1-7 Outubro')
dataR = dataR.replace('2semanavar0210','8-15 Outubro')
dataR = dataR.replace('3semanavar0210','16-24 Outubro')
dataR = dataR.replace('4semanavar0210','25-31 Outubro')
dataR = dataR.replace('1semanavar0211','1-7 Novembro')
dataR = dataR.replace('2semanavar0211','8-15 Novembro')
dataR = dataR.replace('3semanavar0211','16-24 Novembro')
dataR = dataR.replace('4semanavar0211','25-30 Novembro')
dataR = dataR.replace('1semanavar0212','1-7 Dezembro')
dataR = dataR.replace('2semanavar0212','8-15 Dezembro')
dataR = dataR.replace('3semanavar0212','16-24 Dezembro')
dataR = dataR.replace('4semanavar0212','25-31 Dezembro')


dataR
#plotando
fig = px.line(dataR, x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
fig.update_xaxes(title = 'Períodos Mensais')
fig.update_yaxes(title = 'Quantidade Respostas')
fig.update_layout(autosize=False,width=900,height=600)
fig.update_layout(title={
    'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo',
    'y':0.96,
    'x': 0.1
})


fig.update_traces(opacity=.6)

# MATRIX
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/linhas2.png")
# MATRIX

###################
# Mapa de calor
#MAPA DE CALOR

#selecionando apenas as variaveis que serao utilizadas

dgrafarea03 = df.loc[:,[
'1semanavar059', '2semanavar059', '3semanavar059','4semanavar059',
'1semanavar0510', '2semanavar0510', '3semanavar0510','4semanavar0510',
'1semanavar0511', '2semanavar0511', '3semanavar0511','4semanavar0511',
'1semanavar0512', '2semanavar0512', '3semanavar0512','4semanavar0512','Grupos']]


d07 = dgrafarea03.groupby(['Grupos']).sum().reset_index()
#transformando coluna em linha (apenas para fazer a plotagem)
data1 = pd.melt(d07.reset_index(), id_vars=['Grupos'],
value_vars=[
'1semanavar059', '2semanavar059', '3semanavar059','4semanavar059',
'1semanavar0510', '2semanavar0510', '3semanavar0510','4semanavar0510',
'1semanavar0511', '2semanavar0511', '3semanavar0511','4semanavar0511',
'1semanavar0512', '2semanavar0512', '3semanavar0512','4semanavar0512'],var_name='Semanas', value_name='Quantidade')



data1 = data1.replace('1semanavar059','1-7 Setembro')
data1 = data1.replace('2semanavar059','8-15 Setembro')
data1 = data1.replace('3semanavar059','16-24 Setembro')
data1 = data1.replace('4semanavar059','25-30 Setembro')
data1 = data1.replace('1semanavar0510','1-7 Outubro')
data1 = data1.replace('2semanavar0510','8-15 Outubro')
data1 = data1.replace('3semanavar0510','16-24 Outubro')
data1 = data1.replace('4semanavar0510','25-31 Outubro')
data1 = data1.replace('1semanavar0511','1-7 Novembro')
data1 = data1.replace('2semanavar0511','8-15 Novembro')
data1 = data1.replace('3semanavar0511','16-24 Novembro')
data1 = data1.replace('4semanavar0511','25-30 Novembro')
data1 = data1.replace('1semanavar0512','1-7 Dezembro')
data1 = data1.replace('2semanavar0512','8-15 Dezembro')
data1 = data1.replace('3semanavar0512','16-24 Dezembro')
data1 = data1.replace('4semanavar0512','25-31 Dezembro')

# print(data1)

heatmap_data = pd.pivot_table(data1, values='Quantidade',
                              index='Grupos',
                              columns='Semanas')

# print(heatmap_data)

fig = px.imshow(heatmap_data,
                labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                x=[
'01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
'01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
'01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
'01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
               )
fig.update_layout(
    title='Quantidade de Acesso nas Atividades ao Longo do Tempo',
    xaxis_nticks=36)
fig.update_xaxes(title = 'Períodos Mensais')

# MATRIX
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/linhas3.png")
# MATRIX

###################
# Grafico Dispersão
#codigo para ajeitar as colunas
dfteste = df.loc[:,['notaforum','notawebquest', 'notachamadaregular','notachamadasegunda', 'notaavaliacaofinal', 'notachecklist','Grupos']]

dfteste["auxnotaforum"] = dfteste['notaforum']
dfteste["auxnotawebquest"] = dfteste['notawebquest']
dfteste["auxnotachamadaregular"] = dfteste['notachamadaregular']
dfteste["auxnotachamadasegunda"] = dfteste['notachamadasegunda']
dfteste["auxnotaavaliacaofinal"] = dfteste['notaavaliacaofinal']
dfteste["auxnotachecklist"] = dfteste['notachecklist']
dfteste["auxgrupos"] = dfteste['Grupos']

dfteste['auxnotachamadasegunda1'] =dfteste['auxnotachamadasegunda']
ds= dfteste.groupby(['Grupos','auxnotachamadasegunda1'])['auxnotachamadasegunda'].count().reset_index()
ds.rename(columns={'auxnotachamadasegunda1': 'Nota','auxnotachamadasegunda':'Quantidade de Alunos' }, inplace = True)
ds['Tipo de Avaliação'] = 'Segunda Chamada'
#print(ds)

dfteste['auxnotachamadaregular1'] =dfteste['auxnotachamadaregular']
dr= dfteste.groupby(['Grupos','auxnotachamadaregular1'])['auxnotachamadaregular'].count().reset_index()
dr.rename(columns={'auxnotachamadaregular1': 'Nota','auxnotachamadaregular':'Quantidade de Alunos' }, inplace = True)
dr['Tipo de Avaliação'] = 'Chamada Regular'
#print(dr)

dfteste['auxnotaavaliacaofinal1'] =dfteste['auxnotaavaliacaofinal']
dfl= dfteste.groupby(['Grupos','auxnotaavaliacaofinal1'])['auxnotaavaliacaofinal'].count().reset_index()
dfl.rename(columns={'auxnotaavaliacaofinal1': 'Nota','auxnotaavaliacaofinal':'Quantidade de Alunos' }, inplace = True)
dfl['Tipo de Avaliação'] = 'Avaliacao Final'
#print(dfl)


dff = pd.concat([dr,dfl,ds], ignore_index = True)
dff.reset_index()

# display(dff)

#codigo plotagem
fig = px.scatter(dff, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                 color_discrete_sequence=px.colors.qualitative.Plotly)
fig.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
fig.update_xaxes(title = 'Notas')



fig.update_layout(title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações', 'y':1.0, 'x': 0.1},
    width=850,
    height=550,
)

#fig.update_yaxes(title = 'Quantidade Alunos')
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

# MATRIX
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/linhas4.png")
# MATRIX

###################
# Gráfico de BArra
#ajeitando as colunas para colocar no plot
dfteste = df.loc[:,['notachecklist','Grupos']]
dfteste["auxnotachecklist"] = dfteste['notachecklist']
dfteste["auxgrupos"] = dfteste['Grupos']

dfteste.loc[(dfteste.notachecklist<=20.0) , 'auxnotachecklist'] = "0-20"
dfteste.loc[(dfteste.notachecklist>20.0) & (dfteste.notachecklist<=40.0) , 'auxnotachecklist'] = "20-40"
dfteste.loc[(dfteste.notachecklist>40.0) & (dfteste.notachecklist<=60.0) , 'auxnotachecklist'] = "40-60"
dfteste.loc[(dfteste.notachecklist>60.0) & (dfteste.notachecklist<=80.0) , 'auxnotachecklist'] = "60-80"
dfteste.loc[(dfteste.notachecklist>80.0) & (dfteste.notachecklist<=100.0) , 'auxnotachecklist'] = "80-100"


dfteste['auxnotachecklist1'] =dfteste['auxnotachecklist']
d= dfteste.groupby(['Grupos','auxnotachecklist1'])['auxnotachecklist'].count().reset_index()
d.rename(columns={'auxnotachecklist1': 'Média','auxnotachecklist':'Quantidade' }, inplace = True)
d['Tipo de Avaliação'] = 'Checklist'

# print(d)

#codigo para plotagem

fig = px.histogram(d, x='Média', y="Quantidade",color='Grupos', barmode='group',height=400)
fig.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
fig.update_layout(autosize=False,width=900,height=600)
fig.update_layout(title={
    'text' : 'Composição de Alunos por Notas na Avaliação Checklist',
    'y':0.96,
    'x': 0.1
})
fig.update_xaxes(title = 'Intervalo de Notas')
fig.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
fig.update_yaxes(title = 'Quantidade Alunos')
# MATRIX
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/linhas5.png")
# MATRIX

# fig = px.bar(d,x='Média' ,y='Quantidade', color="Grupos", title="Quantidade de Alunos por Notas Checklist",color_discrete_sequence=px.colors.qualitative.Plotly)
