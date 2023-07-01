#Libs

import pandas as pd
import requests

#libs gráficas
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Streamlit
import streamlit as st
from streamlit_lottie import st_lottie

# Configurando a página
st.set_page_config(
    page_title="Tech-Challenge",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto criado para o *tech-challenge* do curso de pós-graduação da FIAP/Alura."
    }
)

#Lendo a base de dados e tratanto a base de dados
valor_futuro = pd.read_csv('Assets/DataFrames/valor_futuro.csv')
valor_futuro["ano"] = pd.to_datetime(valor_futuro["ano"], format='%Y')
economia_mundial = pd.read_csv('Assets/DataFrames/economia_mundial_merge.csv')
exportacoes_ultimos_15_anos = pd.read_csv('Assets/DataFrames/exportacoes_ultimos_15_anos.csv')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.drop(exportacoes_ultimos_15_anos.columns[0], axis='columns')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.set_index('pais_de_destino')

#Titulo de Página
st.title('Análise de Dados: Explorando dados de Exportação Vinícola do Estado do Rio Grande do Sul')

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Importando animação do Lottie
url = requests.get(
    "https://assets10.lottiefiles.com/private_files/lf30_kxzary5v.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in URL")

# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔷Início",
                                                    "📝Dados", 
                                                    "🌎Fatores Externos",
                                                    "📊BI",
                                                    "🏅Ranking",
                                                    "📈Prospecção Futura",
                                                    "📑Referências"])

# Separando as Tabs
with tab0:
    '''
    ## Análise de dados de Exportação Vinícola do Estado do Rio Grande do Sul

    '''
    # Adicionando uma animação do Lottie (Imagem de garrafa e taça de vinho)
    st_lottie(url_json,
          # mudar direção da animação
          reverse=False,
          # Altura e largura da animação
          height=200,  
          width=200,
          # velocidade da animação
          speed=1.25,  
          # repetir animação
          loop=True,  
          # qualidade dos elementos da animação
          quality='high',
           # Identificador da animação
          key='Vinho' 
          )
    '''

    Links importantes:

    http://vitibrasil.cnpuv.embrapa.br/ - Dados de exportação do Rio Grande do Sul

    https://www.embrapa.br/ - Base de dados Embrapa

    Links dos integrantes do projeto:

    https://github.com/GabrielPCO/tech_challenge - Github Gabriel Oliveira

    https://github.com/jackson-simionato/fase1_pos_tech_challenge_wine - Github Jackson Simionato

    gabrielpcoliveira@gmail.com - Email Gabriel Oliveira

    simionato.jackson@gmail.com - Email Jackson Simionato

    haendelf@hotmail.com - Email Haendel Oliveira

    '''
    st.divider()
    '''
    
    ## Resumo:

    Neste documento é apresentada uma análise econômica das exportações internacionais de vinho do Estado do Rio Grande do Sul. Cada aba do documento procura estudar uma faceta diferente dos dados de exportação a fim de reunir informações relevantes para a toma de decisão estratégica de uma empresa brasileira exportadora de vinhos.

    Aqui serão apresentadas análises referentes aos dados gerais de exportação vinifera, uma visão geral da exportação internacional brasileira, o preço médio exercido na exportação de vinho em diferentes países, a interferência de variáveis como clima, demografia e economia sobre os dados de exportação, ranking dos maiores exportadores e um estudo de possíveis ações futuras para o êxito da empresa.

    Para tal, utilizamos dados públicos de um período de 15 anos (entre 2007 a 2021) fornecidos pela Empresa Brasileira de Pesquisa Agropecuária (Embrapa), orgão vinculado ao Ministério da Agricultura e Pecuária (Mapa), que foi criada em 1973 para desenvolver a base tecnológica de um modelo de agricultura e pecuária genuinamente tropical.

    Foram avaliados nesse documento os dados de exportação exclusivamente de vinho de mesa (tinto, branco e rosado). No entando, a base também disponibiliza os dados de exportação de espumantes, uvas frescas e suco de uva.

    Os demais dados como os climáticos, demográficos e econômicos serão apontados ao longo da análise, tendo sua fonte referenciada na última aba desse documento.

    A seguir, disponibilizamos os dados utilizados para a análise no momento da publicação deste documento, assim como um quadro com a visão geral das análises gráficas realizadas.

    '''
    st.divider()
    '''

    #### DataFrame de valores cumulativos dos últimos 15 anos de exportação vinícola do estado do Rio Grande do Sul, por país:
    '''

    # Função do botão de Download para converter o DataFrame em .csv
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    # Convertendo o DataFrame em .csv
    csv = convert_df(exportacoes_ultimos_15_anos)

    # Adicionando o DataFrame
    df = pd.DataFrame(exportacoes_ultimos_15_anos)
    st.dataframe(df,use_container_width=True)

    # Botão de Download do DataFrame
    st.download_button(
        label="Download do CSV",
        data=csv,
        file_name='exportacoes_ultimos_15_anos.csv',
        mime='text/csv',
    )

    st.divider()
    '''

    #### Visão geral das exportação do estado do Rio Grande do Sul:
    '''

    # Adicionando imagem do Grafico
    graf_1 = plt.imread('Assets/Graficos/quadro.png')
    st.image(graf_1)

    st.divider()
    '''

    ## Observação:

    Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
    '''

with tab1:
    with st.container():
        '''
        ## Dados da Vitivinicultura:

        '''
        tab1_0, tab1_1 = st.tabs(["🚛Exportacao",
                                  "🍷Preço Médio do Vinho"])
        with tab1_0:
            '''
            ## Maiores Consumidores de Vinho do Estado do Rio Grande do Sul:

            A seguir, podemos verificar quais os países que mais consumiram litros de vinho dentro dos últimos 15 anos de exportações do estado do Rio Grande do Sul.
            '''
            
            # Adicionando imagem do Grafico
            graf_2 = plt.imread('Assets/Graficos/maiores_consumidores.png')
            st.image(graf_2)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            Pelo gráfico podemos notar que o pais que mais importa quantidade de vinhos em litro é a Rússia, seguida do Paraguai que também apresenta um valor significativo de exportação. Cada um dos demais países do top 10 exportam algo em torno de 1 a 3 milhões de litros e estão mais próximos em termos de comparação.

            '''
            st.divider()
            '''

            ## Maiores Exportações de Vinho em Dólares:

            A seguir, podemos verificar quais os países apresentam maior valor (em dólares) em termos de exportação de vinho dentro dos últimos 15 anos das exportações do estado do Rio Grande do Sul.
            '''

            # Adicionando imagem do Grafico
            graf_3 = plt.imread('Assets/Graficos/valor_exportado.png')
            st.image(graf_3)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            Pelo gráfico, podemos observar que o Paraguai apresenta o maior valor de exportação em dólares. Outros dois países que tem um valor significativo de exportação são Rússia e Estados Unidos.
            
            '''
            st.divider()
            '''

            ## Quantidade de Vinho Exportada x Valor em Dólares (US$):

            A seguir, podemos comparar a quantidade de litros de vinho e o valor de exportaração (em dólares US$) dos maiores consumidores de vinho dentro dos últimos 15 anos.
            '''

            # Adicionando imagem do Grafico
            graf_4 = plt.imread('Assets/Graficos/exportacoes_internacionais_bidirecional.png')
            st.image(graf_4)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            Apesar do Paraguai ser o segundo maior pais para o qual o estado exporta em termos absolutos de litros de vinho, ele é o pais com o maior valor de exportação em dólares. Isso pode ocorrer por diversos fatores, sendo um deles que o Paraguai importa maior quantidade de vinhos de alta qualidade (vinhos premium com maior preço médio).
            
            '''
            st.divider()
            '''
            ## Conclusão:

            A análise dos dados apresentados nos gráficos a cima indicam que há uma disparidade entre a quantidade de litros de vinho exportado e o valor de exportação do mesmo em diferêntes países.
            
            Essa disparidade pode ocorrer por diversos fatores, sendo um deles a diferença do preço médio de vinho exportado para diferentes países.
            
            Outros fatores que podem influenciar nas exportações são: clima, demografia e economia dos diversos países para qual o estado exporta atualmente.
            
            Nas próximas abas do documento, iremos analisar esses diferentes fatores a fim de propiciar uma melhor visão sobre a atual conjuntura do mercado de exportação de vinho brasileiro.
            '''
        with tab1_1:
            '''
            ## Preço Médio do Vinho:

            Aqui, foi feito um estudo sobre o preço do vinho exportado internacionalmente.
            
            No gráfico a seguir, podemos observar os 10 países com maior preço médio do litro de vinho exportado pelo estado.
            '''
            graf_5 = plt.imread('Assets/Graficos/preco_medio_bar.png')
            st.image(graf_5)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise:

            É possível perceber que os maiores valores de preço médio do litro de vinho são praticados em países para os quais o estado faz pouca ou nenhuma exportação atualmente. Isso pode indicar possíveis clientes futuros para se estreitar relações comerciais e tornar as vendas mais rentáveis.
            Nesse sentido, é interessante observar como o preço do litro e o valor total de exportação estão correlacionados, pois o ideal é aliar grandes quantidades de vinho a um preço médio por litro elevado.
            
            '''
            st.divider()
            '''

            ## Preço Médio e Total de Litros Exportados:

            Neste gráfico, vemos uma comparação do preço médio e o total de litros de vinho exportado para todos os demais países da análise.
            '''

            graf_6 = plt.imread('Assets/Graficos/preco_medio_scat.png')
            st.image(graf_6)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise:

            Através desse gráfico, é possível ter mais indícios sobre a tendência das váriáveis preço médio do litro e total de litros exportados. Essas variáveis aparentam conter uma proporcionalidade inversa, possívelmente pelo fato da comercialização de grandes quantidades do produto tenderem a baratear o custo do litro de vinho.
            
            Entretanto, vemos algumas exceções como os Estado Unidos, Países Baixos e Reino Unido, que possuem grande volume de compra e um preço médio do litro mais elevado quando comparados aos outros países desta análise.
            
            Outro fator determinante que apontam a relação dessas duas variáveis é o fato de que se pode observar que os maiores preços médios do litro de vinho correspondem a países desenvolvidos economicamente, principalmente do continente europeu. Uma das intepretações possíveis é que tais países têm maior poder de compra e por isso o Brasil consegue praticar um preço mais vantajoso nas negociações, por outro lado isso também pode indicar que são mercados mais exigentes e compram apenas os vinhos de maior qualidade.
            
            '''
            st.divider()

            '''

            ## Conclusão:

            Pela análise, concluímos que países com maior desenvolvimento econômico e países do continente europeu possuem maiores preços médios do litro do vinho. Ao mesmo tempo, esses países podem apresentar uma maior exigência da qualidade dos produtos que serão exportados.
            
            Como uma estratégia para a empresa exportadora de vinhos, seria interessante focar na obtenção e exportação de vinhos de maior qualidade para países tais países visando o aumento do lucro de exportação pela venda de produtos por um maior preço médio.
            
            A seguir, entraremos em fatores externos como clima, demografia e economia dos principais países para os quais o estado exporta atualmente que podem influenciar diretamente na análise da exportação de vinho. 
            '''

with tab2:
    '''
    ## Fatores Externos que Podem Influenciar nas Exportações:

    '''
    tab2_0, tab2_1, tab2_2 = st.tabs(["🌦️Clima",
                                      "🌎Demografia",
                                      "💵Economia"])
    with tab2_0:
        '''
        ## Influência do Clima nas Exportações:

        No gráfico a seguir, podemos observar a temperatura média em relação a quantidade de vinho exportado pelos países de maior exportação dos últimos 15 anos.
        '''
        graf_7 = plt.imread('Assets/Graficos/clima.png')
        st.image(graf_7)
        '''
        ##### Fonte - List of countries by average yearly temperature. Wikipédia.

        ## Análise:

        Pelo gráfico, podemos observar que é possível que a temperatura média de um país possa influenciar na quantidade de vinho exportada. Se observarmos, a Rússia é o país com menor temperatura média e maior exportação de litros de vinho. O Paraguai tembém tem uma das temperaturas médias mais discrepante entre os paises do top 10 e é um dos países de maior exportação. Um análise mais aprofundada e detalhada seria necessária para verificar se temperaturas mais extremas são correlacionadas diretamente a uma maior exportação de vinho.
        '''

        st.divider()

        '''

        ## Conclusão:

        Pela análise, é possível que a temperatura tenha uma influencia na quantidade de vinho exportada. Dois dos maiores consumidores de vinho do estado possuem as média de temperatura mais extremas entre os países do top de exportação.
        
        Seria interessante que a empresa exportadora levasse em conta o clima dos países para o qual irá exportar seus vinhos. Países com clima mais extremos podem apresentar um maior retorno nas vendas da empresa.
        
        Além disso, o tipo de vinho exportado deve levar em conta se o país do cliente alvo apresenta altas ou baixas temperatura, pois diferentes tipos de vinhos, suas respectivas uvas e características como acidez, aroma e sabor podem ser alterados pelo clima local.
        
        Vinho como o Pinot Noir (tinto) e Chardonnay (branco) são ótimos para climas mais quentes, enquanto Malbec (tinto) é um candidato para climas mais frios.
        
        '''
    with tab2_1:
        '''

        ## Demografia das Exportações:

        A seguir, podemos comparar o valor de exportaração (em dólares) e o tamanho da população dos maiores consumidores da vinícola.
        '''

        # Adicionando imagem do Grafico
        graf_8 = plt.imread('Assets/Graficos/demografia_bidirecional.png')
        st.image(graf_8)

        '''
        ##### Fonte - Lista de países por população. Wikipédia.

        ## Análise: 
        
        Pelo gráfico, podemos observar que aparentemente há pouca ou nenhuma correlação entre o tamanho da população e a quantidade de dólares em vinho exportada internacionalmente. Podemos observar inclusive que países com população relativamente pequena comparada em relação aos demais (como o Paraguai) apresentam volumes expressivos de exportação de vinho do estado.
        
        '''
        st.divider()
        '''

        ## Conclusão:

        Pela análise, em um primeiro momento, a população de um pais não é necessariamente uma variável que ditará a quantidade de vinho que o mesmo irá demandar.
        
        Países demograficamente menos exprecivos ainda sim podem ser grandes consumidores de vinho e inclusive fazer parte dos maiores consumidores do produto.
        
        Fatores como a proximidade geográfica, o clima e a cultura local podem ser muito mais decisivos em termos de quantidade exportada de vinho do que a população local de um determinado pais.
        
        Para a empresa exportadora de vinhos, talvez não seja tão produtivo focar exclusivamente no tamanho da população do pais para a qual ela irá exportar, pois existem outros fatores de maior influência sobre o consumo de vinho pelos países analisados.
        
        '''
    with tab2_2:
        '''
        
        ## Economia Global x Exportação:

        A seguir, podemos comparar pelo gráfico de rosca o valor de exportação dos últimos 15 anos com o PIB de cada um dos países com maior consumo de vinho.
        '''
        #Donut
        fig_1 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
        fig_1.add_trace(go.Pie(labels=economia_mundial['paises'], values=economia_mundial['valor_em_us'], name="Exportações"),
                    1, 1)
        fig_1.add_trace(go.Pie(labels=economia_mundial['paises'], values=economia_mundial['pib'], name="PIB"),
                    1, 2)

        # Tamanho do buraco da rosca
        fig_1.update_traces(hole=0.7, hoverinfo="label+percent+name")

        fig_1.update_layout(
            title_text="Comparando as Exportações em Dólares (US$) com o PIB (US$ - valores atualizado em 2023) dos países top 10 em exportação de vinho",
            # Organizando as anotações no gra´fico.
            annotations=[dict(text='Exportações', x=0.165, y=0.5, font_size=20, showarrow=False),
                        dict(text='PIB', x=0.925, y=0.5, font_size=20, showarrow=False)])
        
        st.plotly_chart(fig_1,  use_container_width = True)
        '''
        ##### Fonte - List of countries by GDP (nominal). Wikipédia.

        ## Análise:

        pelos gráficos, podemos observar que países com grande volume de importações em dólares nem sempre são os países que possuem o maior PIB em relação aos demais. Por exemplo, Paraguai é o maior importador em termos de valores em dólares, mas ao mesmo tempo ele é o país com o menor PIB (Produto Interno Bruto) dentre os demais.
        
        No entanto, muito dos países dentre os maiores consumidores de vinho do estado são desenvolvidos e possuem um PIB consideravel. Isso pode indicar que a capacidade econômica de uma nação tem sim uma influência direta no poder aquisitivo de produtos como o vinho brasileiro.
        
        '''
        st.divider()
        '''

        ## Conclusão:

        Pela análise, é possível inferir que o PIB é um fator que deve ser considerado importânte na decisão de estratégia da empresa. Nem sempre os países de maior poder econômico serão os maiores consumidores, porém a chance de um deles ser um grande consumidor é muito elevada.
        '''

with tab3:
    '''
        ## Análise BI:

        A seguir, podemos verificar uma análise mais aprofundada dos dados.
    '''
    st.markdown('<iframe width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNTg1ZjY5NzgtMDAxMS00MDMyLTlmZGMtNDIzZDRmODIzYjM4IiwidCI6IjgxYTI4ZjEwLWUxYTEtNGJmNi04N2FlLWY1MDQ1ZTE0NjBjMCJ9" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)

with tab4:
    '''
    ## Ranking de Exportações ao Longo dos Anos:

    A seguir, podemos verificar o histórico do ranking dos maiores consumidores da vinícula ao longo dos últimos 15 anos.
    '''

    # Adicionando imagem do Grafico
    graf_9 = plt.imread('Assets/Graficos/ranking.png')
    st.image(graf_9)

    '''
    ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
    ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

    ## Análise: 
    
    Pelo gráfico, podemos notar que tanto o Haiti como a Rússia são países que ao longo dos últimos anos vem aumentando de forma significativa a importação de vinho, recentemente se tornando dois dos maiores exportadores da atualidade para a vinícola. No caso da Rússia, o pais parece ser mais errático nas importações, sendo que há anos que importam muito e outros que não importam ou importam muito pouco.

    '''
    st.divider()
    '''

    ## Visão Global:

    A seguir, podemos ter uma visão global da exportação de quantidade de vinho em litros da vinícola.
    '''

    # Adicionando imagem do Grafico
    graf_10 = plt.imread('Assets/Graficos/mundo.png')
    st.image(graf_10)
    
    '''
    ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
    ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

    ## Análise: 
    
    Pelo gráfico, podemos notar que a maioria dos países do top 10 exportações ficam no hemisfério norte, sendo os maiores consumidores a Europa/Asia (Rússia) e a America do Sul (Paraguai).
    
    '''
    st.divider()
    '''

    ## Conclusão:

    Pela análise, podemos verificar ao longo dos anos uma tendência de crescimento das exportações de vinho em países como a Rússia e o Haiti. Também é possível verificar muito dos grandes consumidores de vinho estão no hemisfério norte, mais especificamente na Europa.
    
    Como estratégia para a empresa, seria interessante focar seus esforços para se adequar ao mercado de vinhos Europeu no momento atual. Além disso, a empresa deve se preparar para futuramente atender um mercado mais amplo, levando em conta países de outros continenteas como o Haiti, Paraguai e China que vem apresentando um aumento em suas demandas pelo produto.
    '''

with tab5:
    '''
    ## Prospecções Futuras:

    A seguir, podemos verificar pelo gráfico de linhas o valor cumulativo em dólares de exportações futuras simulado para os próximos 5 anos no estado do Rio Grande do Sul.
    
    Utilizamos o cálculo de valor futuro:
    '''
    st.latex(r'''
    VF = VP(1+i) * n
    ''')
    ''' 
    > *onde:  VF = Valor Futuro, VP = Valor Presente, i = Taxa de Crescimento e n = Período em anos.*
    
    Escolhemos 5 diferentes cenários de crecimento nas exportações, sendo eles: crescimento de 0%, 1%, 2%, 3% e 4% nos próximos 5 anos.
    
    A idéia por trás desse gráfico é dar um norte para a empresa de qual será o possível cenário de exportação de vinhos brasileiros do estado do Rio Grande do Sul.
    
    Dependendo da situação, diferentes estratégias podem ser traçadas para que a exportação do produto não seja prejudicada.
    '''

    # Criando um gráfico de linhas com plotly express
    fig_2 = px.line(valor_futuro, x='ano', y=valor_futuro.columns[2:], color_discrete_sequence=[
                 "black", "orange", "red", "green", "blue", "purple"])
    
    # Adicionando uma linha vertical para separar os valores originaisdos valores futuros no gráfico de prospecção futura
    fig_2.add_vline(x="2021", line_width=3, line_dash="dash", line_color="green")

    # Alterando o layout do gráfico (Tírulo, nome de eixos, etc)
    fig_2.update_layout(
    title="Prospecções Futuras",
    xaxis_title = "Ano",
    yaxis_title="Valores Exportados em Dólares",
    legend_title="Taxa de Crescimento",
    legend={'traceorder':'reversed'},
    font=dict(
        family="Liberation Serif",
        size=20,
        color="black"
    )
    )

    # Adicionando uma anotação no rodapé do gráfico
    fig_2.add_annotation(
    text = (f"Valor original: Valores cumulativos ao longo de 15 anos de exportação (em Dólares Americanos).")
    , showarrow=False
    , x = 0
    , y = -0.20
    , xref='paper'
    , yref='paper' 
    , xanchor='left'
    , yanchor='bottom'
    , xshift=-1
    , yshift=-5
    , font=dict(size=10, color="grey")
    , align="center"
    ,)

    # Mostrando o gráfico no streamlit
    st.plotly_chart(fig_2,  use_container_width = True)
    '''
    ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
    ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..
    '''

    st.divider()
    '''

    ## Conclusão: 
    
    Podemos concluir que futuramente, como uma estratégia visando o aumento de lucros da empresa, seria interessante em um primeiro momento que a empresa focasse na exportação de seus produto para países como Russia, Paraguai e Estados Unidos e países de maior consumo de vinho do continente europeu, pois estes aparentemente tem maior interesse na aquisição de vinhos provindos do Brasil.
    
    Além disso, países como a China e Haiti aparentam ter um potêncial futuro para grandes importações de vinho brasileiro, conforme pode-se observar um aumento expressivo em suas importações ao longo dos anos.
    
    Em um cenário mais desafiador e de baixo crescimento das exportações, seria interessante que a empresa focasse em mercados mais tradicionais como o merdado de vinhos Europeu (Principalmente a Rússia), pois a chance de se realizar negócios lucrativos com tal mercado é maior em termos históricos.
    
    Já em um cenário de maior crescimento das exportações, seria interessante expandir o leque de clientes da empresa, englobando países de crescente demanda de importação de vinhos como os Estados Unidos, Paraguai, Haiti e a China.
    '''

with tab6:
    '''
    ## Referências: 
    
    1. Banco de dados de uva, vinho e derivados. In: Dados da Vitivinicultura. [Bento Gonçalves, RS: Embrapa, Uva e Vinho], 2022. Disponível em: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06. Acessado em: 28 de jun. 2023.

    2. Lista de países por população. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o. Acessado em: 28 de jun. 2023.

    3. List of countries by average yearly temperature. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature. Acessado em: 28 de jun. 2023.
    
    4. List of countries by GDP (nominal). In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal). Acessado em: 28 de jun. 2023.

    5. Matemática financeira. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://pt.wikipedia.org/wiki/Matem%C3%A1tica_financeira. Acessado em: 28 de jun. 2023.
    '''