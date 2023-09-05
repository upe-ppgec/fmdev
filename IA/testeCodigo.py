#from tkinter.tix import InputOnly
from dash import Dash, html, dcc, State, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
#from flask import Flask
from dash.dependencies import Input, Output
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.ensemble import IsolationForest
from IPython.display import display



#nessa funçao vai rodar outlier e agrupamento
def algoritmoDisciplina(dfMC):
    dfMC.fillna(0, inplace=True)
    dfMC2 = dfMC.drop(dfMC.columns[[0, 1,2,3,4,5]], axis=1)
    dfMC2.fillna(0, inplace=True)
    #print(dfMC2)#tirando colunas categoricas para rodar o algoritmo
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
    #algotimo de agrupamento c o df sem outlier e sem dados categoricos
    kmeanModel = KMeans(n_clusters=2) #ja rodei o Elbow é c esse k=2 msm
    kmeanModel.fit(dfSemOuliers2)
    dfSemOuliers['Grupos']=kmeanModel.predict(dfSemOuliers2)
    df = dfSemOuliers
    #isso é so p ficar bonito na hora de plotar os graficos
    df['Grupos'] = df['Grupos'].replace(1,"Grupo 1")
    df['Grupos'] = df['Grupos'].replace(0,"Grupo 0")
    return df, dfSemOuliers, dfSemOuliers2

def ajeitandoColunas(var,df):
    #agrupando para pegar valores das semanas
    d = df.groupby(['Grupos']).sum().reset_index()

    #transformando coluna em linha (apenas para fazer a plotagem)
    data1 = pd.melt(d.reset_index(), id_vars='Grupos',
    value_vars=[
    '1semana'+var+'9', '2semana'+var+'9', '3semana'+var+'9','4semana'+var+'9',
    '1semana'+var+'10', '2semana'+var+'10', '3semana'+var+'10','4semana'+var+'10',
    '1semana'+var+'11', '2semana'+var+'11', '3semana'+var+'11','4semana'+var+'11',
    '1semana'+var+'12', '2semana'+var+'12', '3semana'+var+'12','4semana'+var+'12'], var_name='Semanas', value_name='Quantidade')

    #atualizando o nome (apenas para plotar organizado)

    data1 = data1.replace('1semana'+var+'9','1-7 Setembro')
    data1 = data1.replace('2semana'+var+'9','8-15 Setembro')
    data1 = data1.replace('3semana'+var+'9','16-24 Setembro')
    data1 = data1.replace('4semana'+var+'9','25-30 Setembro')
    data1 = data1.replace('1semana'+var+'10','1-7 Outubro')
    data1 = data1.replace('2semana'+var+'10','8-15 Outubro')
    data1 = data1.replace('3semana'+var+'10','16-24 Outubro')
    data1 = data1.replace('4semana'+var+'10','25-31 Outubro')
    data1 = data1.replace('1semana'+var+'11','1-7 Novembro')
    data1 = data1.replace('2semana'+var+'11','8-15 Novembro')
    data1 = data1.replace('3semana'+var+'11','16-24 Novembro')
    data1 = data1.replace('4semana'+var+'11','25-30 Novembro')
    data1 = data1.replace('1semana'+var+'12','1-7 Dezembro')
    data1 = data1.replace('2semana'+var+'12','8-15 Dezembro')
    data1 = data1.replace('3semana'+var+'12','16-24 Dezembro')
    data1 = data1.replace('4semana'+var+'12','25-31 Dezembro')
    return data1


def dadosGraficos(df):

    #pre processando os dados p ficar organizados para plotar 
    grafArea = df.loc[:,[
    '1semanavar079', '2semanavar079', '3semanavar079','4semanavar079',
    '1semanavar0710', '2semanavar0710', '3semanavar0710','4semanavar0710',
    '1semanavar0711', '2semanavar0711', '3semanavar0711','4semanavar0711',
    '1semanavar0712', '2semanavar0712', '3semanavar0712','4semanavar0712','Grupos']]
    dataArea = ajeitandoColunas("var07",grafArea)
    
    #
    dgraflinha = df.loc[:,[
    '1semanavar029', '2semanavar029', '3semanavar029','4semanavar029',
    '1semanavar0210', '2semanavar0210', '3semanavar0210','4semanavar0210',
    '1semanavar0211', '2semanavar0211', '3semanavar0211','4semanavar0211',
    '1semanavar0212', '2semanavar0212', '3semanavar0212','4semanavar0212',
    'Grupos']]
    dataLinha = ajeitandoColunas("var02",dgraflinha)
    
    #
    dgrafMCA = df.loc[:,[
    '1semanavar059', '2semanavar059', '3semanavar059','4semanavar059',
    '1semanavar0510', '2semanavar0510', '3semanavar0510','4semanavar0510',
    '1semanavar0511', '2semanavar0511', '3semanavar0511','4semanavar0511',
    '1semanavar0512', '2semanavar0512', '3semanavar0512','4semanavar0512','Grupos']]
    dataMCA = ajeitandoColunas("var05",dgrafMCA)
   
    #
    dgrafMCF = df.loc[:,[
    '1semanavar039', '2semanavar039', '3semanavar039','4semanavar039',
    '1semanavar0310', '2semanavar0310', '3semanavar0310','4semanavar0310',
    '1semanavar0311', '2semanavar0311', '3semanavar0311','4semanavar0311',
    '1semanavar0312', '2semanavar0312', '3semanavar0312','4semanavar0312','Grupos']]
    dataMCF = ajeitandoColunas("var03",dgrafMCF)
 
    # grafico dispersao
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


    dfteste['auxnotaavaliacaofinal1'] =dfteste['auxnotaavaliacaofinal']
    dfl= dfteste.groupby(['Grupos','auxnotaavaliacaofinal1'])['auxnotaavaliacaofinal'].count().reset_index()
    dfl.rename(columns={'auxnotaavaliacaofinal1': 'Nota','auxnotaavaliacaofinal':'Quantidade de Alunos' }, inplace = True)
    dfl['Tipo de Avaliação'] = 'Avaliacao Final'
    
    dff = pd.concat([dr,dfl,ds], ignore_index = True)
    dff.reset_index()
    display(dff)
    dataD = dff

    #grafico barra
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
    dataB = d
    return dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha

###########         DAsh        ###################

df = pd.read_csv('discBiologia_Moodle_filled.csv',encoding = "UTF-8", sep = ";")
df, dfSemOuliers, dfSemOuliers2 = algoritmoDisciplina(df[df['nome_da_disciplina']=='Metodologia cientifica'])
dataB1, dataD1, dataMCF1, dataMCA1, dataA1, dataL1 = dadosGraficos(df)
dataalunos1t = pd.DataFrame()
dataalunos1t['Alunos'] = df['nome_do_aluno']
dataalunos1t['Grupo'] = df['Grupos']
dataalunos1 = dataalunos1t

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.SPACELAB,dbc.icons.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)




#####           plotagem  inicial   por default da paginna        #########
#linha
figL = px.line(dataL1, x="Semanas", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
figL.update_xaxes(title = 'Períodos Mensais')
figL.update_yaxes(title = 'Quantidade Respostas')
figL.update_layout(autosize=True)
figL.update_layout(font = dict(size=10) ,title={ 'text' : 'Quantidade de Respostas nos Fóruns'})
figL.update_traces(opacity=.6)

#area
fig = px.area(dataA1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)
fig.update_layout(autosize=True)
fig.update_layout(font = dict(size=15),title={'text' : 'Quantidade de Visualização ao Ambiente'})
fig.update_xaxes(title = 'Períodos Mensais')
fig.update_yaxes(title = 'Quantidade Visualização')

#mapa de calor
heatmap_data = pd.pivot_table(dataMCA1, values='Quantidade',index='Grupos',columns='Semanas')
figMCA = px.imshow(heatmap_data,
                labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                x=[
'01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
'01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
'01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
'01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto")
figMCA.update_layout(font = dict(size=15),title='Quantidade de Acesso as Atividades ')
figMCA.update_xaxes(title = 'Períodos Mensais')

#Mapa de calor forum
heatmap_data = pd.pivot_table(dataMCF1, values='Quantidade',index='Grupos',columns='Semanas')
figMCF = px.imshow(heatmap_data,
                labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
               x=[
'01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
'01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
'01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
'01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
               )
figMCF.update_layout(font = dict(size=15),title='Quantidade de Acesso aos Fóruns')
figMCF.update_xaxes(title = 'Períodos Mensais')



#Dispersão
figD = px.scatter(dataD1, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',color_discrete_sequence=px.colors.qualitative.Plotly)
figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
figD.update_xaxes(title = 'Notas')
figD.update_layout(font = dict(size=15),title={'text':'Quantidade de Alunos por Notas nas Avaliações'})
figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

#barra
figB = px.histogram(dataB1, x='Média', y="Quantidade",color='Grupos', barmode='group')
figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
figB.update_layout(autosize=True)
figB.update_layout(font = dict(size=15),title={ 'text' : 'CQuantidade de Alunos por Notas na Avaliação Checklist'})
figB.update_xaxes(title = 'Intervalo de Notas')
figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
figB.update_yaxes(title = 'Quantidade Alunos')


summary = {"Alunos na Disciplina": "100"," Respostas nos Fóruns": "5K",
           "Acesso ao Ambiente": "6K"}


#funçao dos cards
def make_card(title, amount):
    return dbc.Card(
        [
            dbc.CardHeader(html.H2(title)),
            dbc.CardBody(html.H3(amount, id=title)),
        ],
        className="text-center shadow",
    )





#####                    HTML                     ##########
app.layout = html.Div(children=[
    html.H1(children='Engajamento em Ambientes EaD',style={ 'fontSize': 40, "font-style": "italic","color":"#373535",'margin-left':'10px'}),
    html.H2(children='Dashboard',style={ 'fontSize': 20, "font-style": "italic", "color":"#777777",'margin-left':'10px'}),
    html.Hr(),

    html.Label(['Selecione:'],style={'fontSize': 20, "font-style": "italic", "color":"#777777",'margin-left':'10px'}),

    html.Div(
        [
        html.Div([
            #html.Label(['Escolha a Disciplina:'],style={'fontSize': 20, "font-style": "italic", 'margin-left':'10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[

                    {'label': 'Disciplina 1', 'value': 'graph1'},
                    {'label': 'Disciplina 2', 'value': 'graph2'},
                        ],
                value='graph1',

                #value='graph1',
                style={"width": "80%",'margin-left':'20px','fontSize': 15, "font-style": "Arial", "color":"#373535"})],className='six columns'),

        html.Div([
            #html.Label(['Escolha o Grupo:'],style={'fontSize': 20, "font-style": "italic", 'margin-left':'20px'}),
            dcc.Dropdown(
                id='demo_dropdown_grupo',
                options=[
                    {'label': 'Todos os Grupos', 'value': 'Todos'},
                    {'label': 'Grupo 0', 'value': 'Grupo 0'},
                    {'label': 'Grupo 1', 'value': 'Grupo 1'},
                        ],
                value='Todos',
                style={"width": "80%",'margin-left':'28px','fontSize': 15, "font-style": "Arial", "color":"#373535"},)],className='six columns')
    ],className='row'),


    html.Br(),
    html.Br(),


    html.Label(['Informações Gerais:'],style={'fontSize': 20, "font-style": "italic", "color":"#777777", 'margin-left':'10px'}),

    html.Div(
        [

        html.Div([
            dbc.Container(
                dbc.Row([dbc.Col(make_card(k, v)) for k, v in summary.items()],
                        className="my-4"),
                        id='card',
                fluid=True,
            style={"width": "90%", 'fontSize': 15, "font-style": "Arial", "color":"#373535"})],className='six columns'),

        html.Div([
            dbc.Container(
                dash_table.DataTable(
                    dataalunos1.to_dict("records"),
                    [{"name": i, "id": i} for i in dataalunos1.columns],
                    id="table_cb",
                    style_cell={'textAlign': 'left','fontSize': 15, "font-style": "Arial", "color":"#373535"},
                    page_size=10,
                    style_table={'height': '200px', "width": "90%",'overflowY': 'auto','margin-left':'52px'},
                    style_cell_conditional=[
                        {'if': {'column_id': 'Alunos'},
                        'width': '100px'},
                        {'if': {'column_id': 'Grupo'},
                        'width': '40px'}]

            ),fluid=True)],className='six columns'),

    ],className='row'),



    html.Label(['Visualizações:'],style={'fontSize': 20, "font-style": "italic", "color":"#777777",'margin-left':'10px'}),
    html.Div(
        [
        html.Div([
            dbc.Container(
                dcc.Graph(
                    id='example-graph',
                    figure=fig,
                    style={"width": "100%"}),fluid=True)],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-linha',
                figure=figL,
                style={"width": "100%"})],className='six columns')
    ],className='row'),

    html.Br(),
    html.Br(),

    html.Div(
        [
        html.Div([
            dcc.Graph(
                id='graf-MCF',
                figure=figMCF,
                style={"width": "100%"})],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-MCA',
                figure=figMCA,
                style={"width": "100%"})],className='six columns'),

    ],className='row'),
    html.Br(),
    html.Br(),

    html.Div(
        [
        html.Div([
            dcc.Graph(
                id='graf-Dispersao',
                figure=figD,
                style={"width": "100%"})],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-Barra',
                figure=figB,
                style={"width": "100%"})],className='six columns'),

    ],className='row'),



],style={'margin-left':'20px','margin-right':'20px'})


#funçaoa para plotar os graficos de acordo com os filtros
def plotGraficos(dataA1,dataL1,dataMCA1,dataB1,dataD1,dataMCF1,dataalunos1,summary,color_graficos,color_mapas):
        fig = px.area(dataA1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=color_graficos)
        fig.update_layout(autosize=True)
        fig.update_layout(font = dict(size=15) , title={'text' : 'Quantidade de Visualização no Ambiente'})
        fig.update_xaxes(title = 'Períodos Mensais')
        fig.update_yaxes(title = 'Quantidade Visualização')
        fig.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        fig.update_xaxes(title_font_family="Arial")
        #
        figL = px.line(dataL1, x="Semanas", y="Quantidade", color='Grupos',color_discrete_sequence=color_graficos)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=15),title={'text' : 'Quantidade de Respostas nos Fóruns'})
        figL.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        figL.update_xaxes(title_font_family="Arial")
        #
        heatmap_data = pd.pivot_table(dataMCA1, values='Quantidade',index='Grupos',columns='Semanas')
        figMCA = px.imshow(heatmap_data,color_continuous_scale=color_mapas,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ 
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto")
        figMCA.update_layout(font = dict(size=15),title='Quantidade de Acesso as Atividades')
        figMCA.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        figMCA.update_xaxes(title_font_family="Arial")
        figMCA.update_xaxes(title = 'Períodos Mensais')
        #
        figD = px.scatter(dataD1, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',color_discrete_sequence=color_graficos)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=15) ,title={'text':'Quantidade de Alunos por Notas nas Avaliações'})
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
        figD.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        figD.update_xaxes(title_font_family="Arial")
        #
        figB = px.histogram(dataB1, x='Média', y="Quantidade",color='Grupos', barmode='group',color_discrete_sequence=color_graficos)
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=15) ,title={'text' : 'Quantidade de Alunos por Notas na Avaliação Checklist'})
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')
        figB.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        figB.update_xaxes(title_font_family="Arial")

        #
        heatmap_data = pd.pivot_table(dataMCF1, values='Quantidade',index='Grupos',columns='Semanas')
        figMCF = px.imshow(heatmap_data,color_continuous_scale=color_mapas,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto")
        figMCF.update_layout(font = dict(size=15),title='Quantidade de Acesso aos Fóruns')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        figMCF.update_layout(font_family="Arial",font_color="#373535",title_font_family="Arial",title_font_color="#373535",legend_title_font_color="#373535")
        figMCF.update_xaxes(title_font_family="Arial")
        #


        return fig,figL,figMCA,figD,figB,figMCF, dataalunos1.to_dict("records"),dbc.Row([dbc.Col(make_card(k, v)) for k, v in summary.items()],className="my-4")



########## chamadas dos componentes HTML ###############
@app.callback([

    Output('example-graph', 'figure'),
    Output('graf-linha', 'figure'),
    Output('graf-MCA', 'figure'),
    Output('graf-Dispersao', 'figure'),
    Output('graf-Barra', 'figure'),
    Output('graf-MCF', 'figure'),
    Output("table_cb", "data"),
    Output('card', 'children'),

], [Input('dropdown', 'value'), Input("demo_dropdown_grupo", "value")])



#######             funçoes de atualização do dash        #############
def multi_output(input_dropdown,input_demo_dropdown_grupo):
    df = pd.read_csv('discBiologia_Moodle_filled.csv',encoding = "UTF-8", sep = ";")
    dfMC , dfSemOuliers, dfSemOuliers2 = algoritmoDisciplina(df[df['nome_da_disciplina']=='Metodologia cientifica'])
    dfZI , dfSemOuliers, dfSemOuliers2 = algoritmoDisciplina(df[df['nome_da_disciplina']=='Zoologia invertebrados'])

    if input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Todos':
        df = dfMC
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        summary = {"Alunos na Disicplina": len(dataalunos1),
                   "Respostas nos Fóruns": dataL1['Quantidade'].sum(),
           "Acesso ao Ambiente": dataA1['Quantidade'].sum()}
        color_graficos=px.colors.qualitative.Plotly
        color_mapas='RdBu'
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1, summary,color_graficos,color_mapas)
    
    elif input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Grupo 1':
        df = dfMC
        df = df[df["Grupos"]== 'Grupo 1']
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        color_graficos=px.colors.qualitative.Set1
        color_mapas='reds'

        summary = {"Alunos no Grupo 1": len(dataalunos1),
                   "Respostas nos Fóruns": dataLinha['Quantidade'].sum(),
           "Acesso ao Ambiente": dataArea['Quantidade'].sum()}   
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1,summary,color_graficos,color_mapas)

    elif input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Grupo 0':
        df = dfMC
        df = df[df["Grupos"]== 'Grupo 0']
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        summary = {"Alunos no Grupo 0": len(dataalunos1),
                   "Respostas nos Fóruns": dataLinha['Quantidade'].sum(),
           "Acesso ao Ambiente": dataArea['Quantidade'].sum()}  
        color_graficos=px.colors.qualitative.Plotly
        color_mapas='blues'  
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1,summary,color_graficos,color_mapas)
    
    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Grupo 0':
        df = dfZI
        df = df[df["Grupos"]== 'Grupo 0']
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        summary = {"Alunos no Grupo 0": len(dataalunos1),
                   "Respostas nos Fóruns": dataLinha['Quantidade'].sum(),
           "Acesso ao Ambiente": dataArea['Quantidade'].sum()}
        color_graficos=px.colors.qualitative.Plotly
        color_mapas='blues'
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1,summary,color_graficos,color_mapas)
    

    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Grupo 1':
        df = dfZI
        df = df[df["Grupos"]== 'Grupo 1']
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        summary = {"Alunos no Grupo 1": len(dataalunos1),
                   "Respostas nos Fóruns": dataLinha['Quantidade'].sum(),
           "Acesso ao Ambiente": dataArea['Quantidade'].sum()}
        color_graficos=px.colors.qualitative.Set1
        color_mapas='reds'
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1,summary,color_graficos,color_mapas)

    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Todos':
        df = dfZI
        dataB, dataD, dataMCF, dataMCA, dataArea, dataLinha = dadosGraficos(df)
        dataalunos1t = pd.DataFrame()
        dataalunos1t['Alunos'] = df['nome_do_aluno']
        dataalunos1t['Grupo'] = df['Grupos']
        dataalunos1 = dataalunos1t
        summary = {"Alunos na Disciplina": len(dataalunos1),
                   "Respostas nos Fóruns": dataLinha['Quantidade'].sum(),
           "Acesso ao Ambiente": dataArea['Quantidade'].sum()}
        color_graficos=px.colors.qualitative.Plotly
        color_mapas='RdBu'
        return plotGraficos(dataArea, dataLinha, dataMCA,dataB, dataD, dataMCF, dataalunos1,summary,color_graficos,color_mapas)
    
    else:
        pass


#chamada web
if __name__ == '__main__':
    app.run(debug=True)