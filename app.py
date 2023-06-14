#Libs

import pandas as pd

#libs gráficas
import matplotlib.pyplot as plt

#Streamlit
import streamlit as st

#Lendo a base de dados e tratanto a base de dados
exportacoes_ultimos_15_anos = pd.read_csv('Assets/DataFrames/exportacoes_ultimos_15_anos.csv')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.drop(exportacoes_ultimos_15_anos.columns[0], axis='columns')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.set_index('pais_de_destino')

#Titulo de Página
st.title('Visão Econômica: Explorando dados de Exportação Internacional da Vinícula do Estado do Rio Grande do Sul')

# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Início",
                                                          "Maiores Consumidores", 
                                                          "Valor Exportado", 
                                                          "Visão Geral ", 
                                                          "Demografia", 
                                                          "Ranking",
                                                          "Mundo",
                                                          "Prospecção Futura"])

# Separando as Tabs
with tab0:
    '''
    ## Visão Econômica da Vinícula do Estado do Rio Grande do Sul

    Links importantes:

    http://vitibrasil.cnpuv.embrapa.br/

    Base de dados Embrapa

    https://www.embrapa.br/

    Neste documento é apresentada uma análise econômica das exportações internacionais da vínicula do Estado do Rio Grande do Sul. Cada aba do documento procura estudar uma faceta diferente dos dados de exportação da vinícula.

    Aqui serão apresentadas análises referentes a quantidade de litros exportados, valor de exportação, visão geral da exportação internacional, a demografia das exportações, ranking dos maiores exportadores e uma visão global da situação das exportações da Vinícula do Estado do Rio Grande do Sul.

    Para tal, utilizamos dados públicos de um período de 15 anos (entre 2007 a 2021) fornecidos pela Empresa Brasileira de Pesquisa Agropecuária (Embrapa), orgão vinculado ao Ministério da Agricultura e Pecuária (Mapa), que foi criada em 1973 para desenvolver a base tecnológica de um modelo de agricultura e pecuária genuinamente tropical.

    A seguir, disponibilizamos os dados utilizados para a análise no momento da publicação deste documento, assim como um gráfico com a visão geral das análises realizadas.

    '''
    # Adicionando o DataFrame
    df = pd.DataFrame(exportacoes_ultimos_15_anos)
    st.dataframe(df,use_container_width=True)

    # Adicionando imagem do Grafico
    graf_1 = plt.imread('Assets/Graficos/quadro.png')
    st.image(graf_1)

with tab1:
    '''
    ## Resumo:

    A seguir, podemos verificar quais os países que mais consumiram litros de vinho dentro dos últimos 15 anos de exportações da vinícula.
    '''
    
    # Adicionando imagem do Grafico
    graf_2 = plt.imread('Assets/Graficos/maiores_consumidores.png')
    st.image(graf_2)

    '''
    ## Análise: 
    
    Pelo gráfico podemos notar que o pais que mais importa quantidade de vinhos em litro é a Rússia, seguida do Paraguai que também apresenta um valor significativo de exportação. Os demais países do top 10 apresentam uma quantidade de exportação que varia entre 1 a 3 milhões de litros e estão mais próximos em termos de comparação.
    '''

with tab2:
    '''
    ## Resumo:

    A seguir, podemos verificar quais os países com maior importaração de vinho (em dólares) dentro dos últimos 15 anos de exportações da vinícula.
    '''

    # Adicionando imagem do Grafico
    graf_3 = plt.imread('Assets/Graficos/valor_exportado.png')
    st.image(graf_3)

    '''
    ## Análise: 
    
    Pelo gráfico, podemos observar que o Paraguai apresenta o maior valor de exportação em dólares. Outros dois países que tem um valor significativo de exportação são Rússia e Estados Unidos.
    '''

with tab3:
    '''
    ## Resumo:

    A seguir, podemos comparar a quantidade de litros de vinho e o valor de exportaração (em dólares) dos maiores consumidores da vinícula dentro dos últimos 15 anos.
    '''

    # Adicionando imagem do Grafico
    graf_4 = plt.imread('Assets/Graficos/exportacoes_internacionais_bidirecional.png')
    st.image(graf_4)
    '''
    ## Análise: 
    
    Apesar do Paraguai ser o segundo maior pais para o qual a vinícula exporta em termos absolutos de litros de vinho, ele é o pais com o maior valor de exportação em dólares. Isso pode ocorrer por diversos fatores, sendo um deles que o Paraguai importa maior quantidade de vinhos de alta qualidade da vinícula (vinhos premium que são mais caros).
    '''

with tab4:
    '''
    ## Resumo:

    A seguir, podemos comparar o valor de exportaração (em dólares) e o tamanho da população dos maiores consumidores da vinícula.
    '''

    # Adicionando imagem do Grafico
    graf_5 = plt.imread('Assets/Graficos/demografia_bidirecional.png')
    st.image(graf_5)
    '''
    ## Análise: 
    
    Pelo gráfico, podemos observar que aparentemente há pouca ou nenhuma correlação entre o tamanho da população e a quantidade de dólares em vinho exportada internacionalmente. Podemos observar inclusive que países com população relativamente pequena comparada em relação aos demais (como o Paraguai) tem volumes expressivos de exportação para a vinícula.
    '''

with tab5:
    '''
    ## Resumo:

    A seguir, podemos verificar o histórico do ranking dos maiores consumidores da vinícula ao longo dos últimos 15 anos.
    '''

    # Adicionando imagem do Grafico
    graf_6 = plt.imread('Assets/Graficos/ranking.png')
    st.image(graf_6)
    '''
    ## Análise: 
    
    Pelo gráfico, podemos notar que tanto o Haiti como a Rússia são países que ao longo dos últimos anos vem aumentando de forma significativa a importação de vinho, recentemente se tornando dois dos maiores exportadores da atualidade para a vinícula. No caso da Rússia, o pais parece ser mais errático nas importações, sendo que há anos que importam muito e outros que não importam ou importam muito pouco.
    '''

with tab6:
    '''
    ## Resumo:

    A seguir, podemos ter uma visão global da exportação de quantidade de vinho em litros da vinícula.
    '''

    # Adicionando imagem do Grafico
    graf_7 = plt.imread('Assets/Graficos/mundo.png')
    st.image(graf_7)
    '''
    ## Análise: 
    
    Pelo gráfico, podemos notar que a maioria dos países do top 10 exportações ficam no hemisfério norte, sendo os maiores consumidores a Europa/Asia (Rússia) e a America do Sul (Paraguai).
    '''

with tab7:
    '''
    ## Conclusão: 
    
    Podemos concluir que futuramente, como uma estratégia visando o aumento de lucros da empresa, seria interessante que a vinícula focasse na exportação de seus produto para países como Paraguai, Russia e Estados Unidos, pois estes aparentemente tem maior interesse na aquisição de vinhos provindos da vinícula.

    Além disso, países como a China e Haiti aparentam ter um potêncial futuro para grandes importações de vinho da vinícula, conforme pode-se observar um aumento expressivo em suas importações ao longo dos anos.
    '''