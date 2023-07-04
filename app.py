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
@st.cache_data
def read_csv_file(file):
    return pd.read_csv(file)

@st.cache_data
def transform_to_datetime(df, string):
    return pd.to_datetime(df, format=string)

valor_futuro = read_csv_file('Assets/DataFrames/valor_futuro.csv')
valor_futuro["ano"] = transform_to_datetime(valor_futuro["ano"], '%Y')
economia_mundial = read_csv_file('Assets/DataFrames/economia_mundial_merge.csv')
exportacoes_ultimos_15_anos = read_csv_file('Assets/DataFrames/exportacoes_ultimos_15_anos.csv')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.drop(exportacoes_ultimos_15_anos.columns[0], axis='columns')
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.rename(columns={'pais_de_destino' : 'Destino', 'pais_de_origem_brasil' : 'Origem', 'quantidade_em_litros_de_vinho_exportado' : 'Litros de vinho', 'valor_em_us' : 'Valor em dólares'})
exportacoes_ultimos_15_anos = exportacoes_ultimos_15_anos.set_index('Destino')

#Titulo de Página
st.title('Análise de dados: explorando dados de exportação vinícola do Estado do Rio Grande do Sul')

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

@st.cache_data
def load_url(url):
    return requests.get(
    url)

# Importando animação do Lottie
url = load_url("https://assets10.lottiefiles.com/private_files/lf30_kxzary5v.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in URL")

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

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
    ## Análise de dados de exportação vinícola do Estado do Rio Grande do Sul

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

    Neste documento é apresentada uma análise econômica das exportações internacionais de vinho do Estado do Rio Grande do Sul. Cada aba do documento procura estudar uma faceta diferente dos dados de exportação a fim de reunir informações relevantes para a tomada de decisão estratégica de uma empresa brasileira exportadora de vinhos.

    Aqui serão apresentadas análises referentes aos dados gerais de exportação vinífera, uma visão geral da exportação internacional brasileira, o preço médio exercido na exportação de vinho em diferentes países, a interferência de variáveis como clima, demografia e economia sobre os dados de exportação, ranking dos maiores exportadores e um estudo de possíveis ações futuras para o êxito da empresa.

    Para tal, utilizamos dados públicos de um período de 15 anos (entre 2007 a 2021) fornecidos pela Empresa Brasileira de Pesquisa Agropecuária (Embrapa), órgão vinculado ao Ministério da Agricultura e Pecuária (Mapa), que foi criada em 1973 para desenvolver a base tecnológica de um modelo de agricultura e pecuária genuinamente tropical.

    Foram avaliados nesse documento os dados de exportação exclusivamente de vinho de mesa (tinto, branco e rosado). No entanto, a base original também disponibiliza os dados de exportação de espumantes, uvas frescas e suco de uva.

    Os demais dados como os climáticos, demográficos e econômicos serão apontados ao longo da análise, tendo sua fonte referenciada na última aba desse documento.

    A seguir, disponibilizamos os dados utilizados para a análise no momento da publicação deste documento, assim como um quadro com a visão geral das análises gráficas realizadas.

    '''
    st.divider()
    '''

    #### DataFrame de valores cumulativos dos últimos 15 anos de exportação vinícola do estado do Rio Grande do Sul, por país
    '''

    # Função do botão de Download para converter o DataFrame em .csv
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    # Convertendo o DataFrame em .csv
    csv = convert_df(exportacoes_ultimos_15_anos)

    # Adicionando o DataFrame
    @st.cache_data
    def create_df(df):
        return pd.DataFrame(df)
    
    dataframe = create_df(exportacoes_ultimos_15_anos)
    st.dataframe(dataframe, use_container_width=True)

    # Botão de Download do DataFrame
    st.download_button(
        label="Download do CSV",
        data=csv,
        file_name='exportacoes_ultimos_15_anos.csv',
        mime='text/csv',
    )

    st.divider()
    '''

    #### Visão geral das exportações do Estado do Rio Grande do Sul
    '''

    # Adicionando imagem do Grafico
    graf_1 = load_img('Assets/Graficos/quadro.png')
    st.image(graf_1)

    st.divider()
    '''

    ## Observação:

    Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
    '''

with tab1:
    with st.container():
        '''
        ## Dados da Vitivinicultura do Estado do Rio Grande do Sul

        '''
        tab1_0, tab1_1 = st.tabs(["🚛Exportacao",
                                  "🍷Preço Médio do Vinho"])
        with tab1_0:
            '''
            ## Total de exportações na série histórica de 1970 a 2021
            Através do gráfico abaixo, é possível visualizar a evolução do montante total de litros de vinho exportados pelo Rio Grande do Sul para o mundo. 
            
            '''

            #Adicionando imagem do Grafico
            graf_1970_2021 = load_img('Assets/Graficos/areaplot_exportacoes_ano_a_ano_acumulado.png')
            st.image(graf_1970_2021)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise:

            A partir da inclinação da curva, nota-se um grande aumento nas exportações a partir da década de 1990, tendência que se repetiu nos anos 2010 após uma pequena redução na década de 2000. Isto indica um comportamento cíclico no total de vinho exportado pelo RS.

            Para as próximas análises, será utilizado um recorte dos últimos 15 anos da série histórica (2007-2021), como foi indicado pela barra vertical no gráfico acima.

            '''
            st.divider()
            '''

            ## Maiores consumidores de vinho do Estado do Rio Grande do Sul

            A seguir, pode-se verificar quais os países que mais consumiram litros de vinho dentro dos últimos 15 anos de exportações do estado do Rio Grande do Sul.
            '''
            
            # Adicionando imagem do Grafico
            graf_2 = load_img('Assets/Graficos/maiores_consumidores.png')
            st.image(graf_2)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            É possível notar que o maior importador em quantidade de vinhos em litro é a Rússia, seguida do Paraguai que também apresenta um valor significativo de importação. Cada um dos demais países do top 10 importam algo em torno de 1 a 3 milhões de litros e estão mais próximos em termos de comparação.

            '''
            st.divider()
            '''

            ## Maiores exportações de vinho em dólares

            A seguir, observa-se quais os países apresentam maior valor (em dólares) em termos de compra de vinho do Rio Grande do Sul dentro dos últimos 15 anos.
            '''

            # Adicionando imagem do Grafico
            graf_3 = load_img('Assets/Graficos/valor_exportado.png')
            st.image(graf_3)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            De acordo com o gráfico, o Paraguai é o maior comprador em termos de valor em dólares. Outros dois países têm um valor significativo neste sentido: Rússia e Estados Unidos.
            
            '''
            st.divider()
            '''

            ## Quantidade de vinho exportada x valor em dólares (US$)

            Através do gráfico abaixo, é possível comparar a quantidade de litros de vinho e o valor de exportação (em dólares US$) dos maiores consumidores de vinho dentro dos últimos 15 anos.
            '''

            # Adicionando imagem do Grafico
            graf_4 = load_img('Assets/Graficos/exportacoes_internacionais_bidirecional.png')
            st.image(graf_4)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise: 
            
            Apesar do Paraguai ser o segundo maior pais para o qual o Rio Grande do Sul exporta em termos absolutos de litros de vinho, ele é o país com o maior valor de exportação em dólares. Isso pode ocorrer por diversos fatores, sendo um deles que o Paraguai importa maior quantidade de vinhos de alta qualidade (vinhos premium com maior preço médio).
            
            '''
            st.divider()
            '''
            ## Exportações ano a ano por país de destino

            Além do montante total acumulado dos últimos 15 anos, informações importantes podem ser obtidas do total exportado por ano em cada um dos 10 principais países importadores de vinho gaúcho, como mostra o gráfico abaixo.
            '''
            # Adicionando imagem do Grafico
            graf_exp_ano_ano = load_img('Assets/Graficos/top10_lineplot_exportacoes_ano_a_ano.png')
            st.image(graf_exp_ano_ano)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise:

            O gráfico de linhas mostra que os dois países para o qual o RS mais exporta vinho possuem comportamentos muito diferentes nos últimos 15 anos. A Rússia é bastante inconstante, com alguns anos comprando quantidades muito grandes de vinho, seguidos de outros períodos em que praticamente não compra a bebida do RS. Possivelmente a Rússia apenas fecha negociações nos momentos mais favoráveis para o país ou então adota a prática de estocar vinhos para anos seguintes.

            Já as exportações para o Paraguai vêm aumento ano após ano, resultando em uma curva muito mais constante. Pode indicar que o Rio Grande do Sul conquistou o mercado paraguaio e cada vez mais mantém uma relação comercial mais próxima.

            '''
            st.divider()
            '''
            ## Conclusão:

            A análise dos dados apresentados nos gráficos acima indica que há uma disparidade entre a quantidade de litros de vinho exportado e o valor de exportação do mesmo em diferentes países.
            
            Essa variação pode ocorrer por uma série de fatores, sendo um deles a diferença do preço médio de vinho exportado para diferentes países.
            
            Outros fatores que podem influenciar nas exportações são: clima, demografia e economia dos diversos países para qual o estado exporta atualmente.
            
            Nas próximas abas do documento, iremos analisar esses diferentes fatores a fim de propiciar uma melhor visão sobre a atual conjuntura do mercado de exportação de vinho brasileiro.
            '''
        with tab1_1:
            '''
            ## Preço médio do vinho

            Nesta seção, tem-se uma visão do preço médio do litro de vinho exportado para cada país
            
            No gráfico a seguir, estão evidenciados os 10 países com os maiores valores de preço médio do litro de vinho.
            '''
            graf_5 = load_img('Assets/Graficos/preco_medio_bar.png')
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

            ## Preço médio e total de litros exportados

            Neste gráfico, é apresentada uma comparação do preço médio e o total de litros de vinho exportado para todos os demais países da análise.
            '''

            graf_6 = load_img('Assets/Graficos/preco_medio_scat.png')
            st.image(graf_6)

            '''
            ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
            ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

            ## Análise:

            Através desse gráfico, é possível ter mais indícios sobre a tendência das variáveis preço médio do litro e total de litros exportados. Essas variáveis aparentam conter uma proporcionalidade inversa, possivelmente pelo fato da comercialização de grandes quantidades do produto tenderem a baratear o custo do litro de vinho.
            
            Entretanto, existem algumas exceções como os Estado Unidos, Países Baixos e Reino Unido, que possuem grande volume de compra e um preço médio do litro mais elevado quando comparados aos outros países desta análise.
            
            Outro fator determinante que apontam a relação dessas duas variáveis é o fato de que se pode observar que os maiores preços médios do litro de vinho correspondem a países desenvolvidos economicamente, principalmente do continente europeu. Uma das intepretações possíveis é que tais países têm maior poder de compra e por isso o Brasil consegue praticar um preço mais vantajoso nas negociações, por outro lado isso também pode indicar que são mercados mais exigentes e compram apenas os vinhos de maior qualidade.
            
            '''
            st.divider()

            '''

            ## Conclusão:

            Pela análise, conclui-se que países com maior desenvolvimento econômico e países do continente europeu possuem maiores preços médios do litro do vinho. Ao mesmo tempo, esses países podem apresentar uma maior exigência da qualidade dos produtos que serão exportados.
            
            Como uma estratégia para a empresa exportadora de vinhos, seria interessante focar na obtenção e exportação de vinhos de maior qualidade para países tais países visando o aumento do lucro de exportação pela venda de produtos por um maior preço médio.
            
            A seguir, serão abordados fatores externos como clima, demografia e economia dos principais países para os quais o estado exporta atualmente que podem influenciar diretamente na análise da exportação de vinho. 
            '''

with tab2:
    '''
    ## Fatores externos que podem influenciar nas exportações

    '''
    tab2_0, tab2_1, tab2_2 = st.tabs(["🌦️Clima",
                                      "🌎Demografia",
                                      "💵Economia"])
    with tab2_0:
        '''
        ## Exportações de vinho e temperatura média anual

        Geralmente, é comum a associação entre clima frio e o consumo de vinho. No Brasil, por exemplo, as vendas de vinho no inverno aumentam drasticamente:
        
        https://www.cnnbrasil.com.br/viagemegastronomia/insiders/voce-provavelmente-esta-bebendo-mais-vinho-mas-sabe-por-que/

        Seguindo essa lógica, países com temperaturas mais baixas possivelmente consomem mais vinho do que países mais quentes. Abaixo vemos um gráfico que relaciona a temperatura média anual de países para o qual o RS exportou vinho e a quantidade de vinho exportada nos últimos 15 anos.
        '''
        graf_temp_exportacao = load_img('Assets/Graficos/lmplot_litros_exportados_temperatura_media.png')
        st.image(graf_temp_exportacao)

        '''
        ##### Fonte - List of countries by average yearly temperature. Wikipédia.
        ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
        ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

        # Análise:

        De acordo com o gráfico, os dados da Embrapa Uva e Vinho e os dados climáticos de cada país sugerem uma correlação negativa entre as variáveis de temperatura média anual do país e o total de vinho importado do Brasil, isto é, há uma tendência dos países de clima mais quente comprarem menos vinho do Brasil em quantidade absoluta.

        Como forma de explorar mais a fundo esta hipótese, também é necessário ponderar o peso demográfico no consumo destes países, pois o tamanho da população de cada país é um fator determinante no consumo absoluto de vinho.
        '''    
        st.divider()
        '''
        ## Exportações de vinho per capita e média anual de temperatura

        Como forma de ponderar o tamanho da população de cada país, o gráfico abaixo relaciona o consumo de vinho per capita e a quantidade de vinho exportada nos últimos 15 anos.
        '''
        graf_temp_exportacao_per_capita = load_img('Assets/Graficos/lmplot_litros_exportados_per_capita_temperatura_media.png')
        st.image(graf_temp_exportacao_per_capita)
        '''
        ##### Fonte - List of countries by average yearly temperature. Wikipédia.
        ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
        ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

        # Análise:

        Neste segundo gráfico, abordando o consumo de vinho relativo ao tamanho da população, vê-se que praticamente não há correlação entre baixas temperaturas e um maior consumo de vinho de acordo com os dados de exportação da Embrapa Uva e Vinho.

        É possível observar que na verdade os maiores valores de litros de vinho por habitante são de países com clima muito quente, como o Paraguai, Haiti e Curaçao. Portanto, apesar da temperatura média anual parecer ter um impacto quando se olha os valores absolutos de vinho importado do Brasil, é preciso ter cautela ao associar as duas variáveis de maneira direta, outros fatores como a economia e a cultura de cada país podem ser mais influentes nesse sentido.
        '''
        st.divider()
        '''
        ## Influência dos aspectos climáticos nos países com maiores exportações

        Por fim, no gráfico a seguir estão destacados os 10 principais países compradores de vinho do RS e como a temperatura média anual destes países varia.
        '''
        graf_7 = load_img('Assets/Graficos/clima.png')
        st.image(graf_7)
        '''
        ##### Fonte - List of countries by average yearly temperature. Wikipédia.

        ## Análise:

        Pelo gráfico, nota-se que a temperatura média de um país pode estar relacionada à quantidade de vinho exportada. Se observarmos, a Rússia é o país com menor temperatura média e maior exportação de litros de vinho. Além disso, 8 dos 10 países possuem temperatura média anual abaixo dos 13ºC. Por outro lado, o Paraguai também tem uma das temperaturas médias mais discrepante entre os países do top 10 e é um dos países de maior exportação. Uma análise mais aprofundada e detalhada seria necessária para verificar se temperaturas mais extremas são correlacionadas diretamente a uma maior exportação de vinho.
        '''

        st.divider()

        '''

        ## Conclusão:

        De acordo com os dados, é possível que a temperatura tenha uma influência na quantidade de vinho exportada. Dois dos maiores consumidores de vinho do estado possuem as médias de temperatura mais extremas entre os países do top de exportação.
        
        Seria interessante que a empresa exportadora levasse em conta o clima dos países para o qual irá exportar seus vinhos. Países com clima mais extremos podem apresentar um maior retorno nas vendas da empresa.
        
        Além disso, o tipo de vinho exportado deve levar em conta se o país do cliente alvo apresenta altas ou baixas temperatura, pois diferentes tipos de vinhos, suas respectivas uvas e características como acidez, aroma e sabor podem ser alterados pelo clima local.
        
        Vinho como o Pinot Noir (tinto) e Chardonnay (branco) são ótimos para climas mais quentes, enquanto Malbec (tinto) é um candidato para climas mais frios.

        Entretanto, associar tais variáveis de maneira direta não parece o correto, fatores como cultura e economia também devem ser levados em conta no momento de definir os países alvo.
        
        '''
    with tab2_1:
        '''

        ## Demografia das exportações

        A seguir, são comparados o valor de exportação (em dólares) e o tamanho da população dos maiores consumidores da vinícola.
        '''

        # Adicionando imagem do Grafico
        graf_8 = load_img('Assets/Graficos/demografia_bidirecional.png')
        st.image(graf_8)

        '''
        ##### Fonte - Lista de países por população. Wikipédia.

        ## Análise: 
        
        Observa-se que aparentemente há pouca ou nenhuma correlação entre o tamanho da população e a quantidade de dólares em vinho exportada internacionalmente. Inclusive, países com população relativamente pequena em relação aos demais (como o Paraguai) apresentam volumes expressivos de exportação de vinho do estado.
        
        '''
        st.divider()
        '''

        ## Conclusão:

        Em um primeiro momento, a população de um país não é necessariamente uma variável que ditará a quantidade de vinho que ele irá demandar.
        
        Países demograficamente menos expressivos ainda sim podem ser grandes consumidores de vinho e inclusive fazer parte dos maiores consumidores do produto.
        
        Fatores como a proximidade geográfica, o clima e a cultura local podem ser muito mais decisivos em termos de quantidade exportada de vinho do que a população local de um determinado país.
        
        Para a empresa exportadora de vinhos, talvez não seja tão produtivo focar exclusivamente no tamanho da população do país para a qual ela irá exportar, pois existem outros fatores de maior influência sobre o consumo de vinho pelos países analisados.
        
        '''
    with tab2_2:
        '''
        
        ## Economia global x exportação

        A seguir, é possível comparar pelo gráfico de rosca o valor de exportação dos últimos 15 anos com o PIB de cada um dos países com maior consumo de vinho.
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

        Os dados indicam que países com grande volume de importações em dólares nem sempre são os países que possuem o maior PIB em relação aos demais. Por exemplo, Paraguai é o maior importador em termos de valores em dólares, mas ao mesmo tempo ele é o país com o menor PIB (Produto Interno Bruto) dentre os demais.
        
        No entanto, muito dos países dentre os maiores consumidores de vinho do estado são desenvolvidos e possuem um PIB considerável. Isso pode indicar que a capacidade econômica de uma nação tem sim uma influência direta no poder aquisitivo de produtos como o vinho brasileiro.
        
        '''
        st.divider()
        '''

        ## Conclusão:

        É possível inferir que o PIB é um fator que deve ser considerado importante na decisão de estratégia da empresa. Nem sempre os países de maior poder econômico serão os maiores consumidores, porém a chance de um deles ser um grande consumidor é muito elevada.
        '''

with tab3:
    '''
        ## Análise BI

        A seguir, podemos verificar uma análise mais aprofundada dos dados.
    '''
    
    st.markdown('<iframe width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNDkzNzZiY2EtZTY4Ny00ZDEyLWE5NWUtYzFkNTZjNjVlYzM1IiwidCI6IjgxYTI4ZjEwLWUxYTEtNGJmNi04N2FlLWY1MDQ1ZTE0NjBjMCJ9" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
    
    '''
        
        ## Análise:

        Analisando os países com maior valor gasto com importações de vinhos temos o cenário abaixo:

            Paraguai: Teve um aumento de 85% nas importações de vinho ao longo do período;
        
            Rússia: Apresentou um pico em 2013 e, a partir dali uma queda de -98%;
        
            Estados Unidos: Notamos que vem em uma média constante, porém em 2021 houve uma redução na importação de -67%;
        
            Reino unido: notamos uma forte oscilação da importação ano a ano durante o período apurado;
        
            China: analisando o histórico podemos perceber que em 2009 tivemos um aumento de 1761% para importação desde então mantem com uma mediana de US$ 279.956;
        
            Países Baixos: analisando o histórico notamos que está em queda constante a cada ano, chegando em importar em 2021 apenas US$ 8.000.

        Analisando o pico de 23M de 2013:

            Notamos que a Rússia teve uma participação de 15M considerando assim um outlier para essa análise.

        ## Conclusão:

        Pelo que se pode observar na análise do período dos últimos 15 anos, o Paraguai é um dos países mais promissores para uma possível operação de exportação de vinhos brasileiros.
        
        Além disso, a China também vem sendo um mercado que cresce constantemente em termos de importação de vinhos do Brasil. Esse país deve ser considerado para futuras negociações da exportadora.

        Rússia, Estados Unidos e outros países do continente europeu ainda são opções viáveis para negociações, porém em breve podem entrar em um período de declínio de seu consumo de vinho brasileiro, acarretando perdas financeiras para a empresa.
    '''
with tab4:
    '''
    ## Ranking de exportações ao longo dos anos

    A seguir, podemos verificar o histórico do ranking dos maiores consumidores da vinícola ao longo dos últimos 15 anos.
    '''

    # Adicionando imagem do Grafico
    graf_9 = load_img('Assets/Graficos/ranking.png')
    st.image(graf_9)

    '''
    ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
    ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

    ## Análise: 
    
    Pelo gráfico, podemos notar que tanto o Haiti como a Rússia são países que ao longo dos últimos anos vem aumentando de forma significativa a importação de vinho, recentemente se tornando dois dos maiores exportadores da atualidade para a vinícola. No caso da Rússia, o país parece ser mais errático nas importações, sendo que há anos que importam muito e outros que não importam ou importam muito pouco.

    '''
    st.divider()
    '''

    ## Visão global

    A seguir, podemos ter uma visão global da exportação de quantidade de vinho em litros da vinícola.
    '''

    # Adicionando imagem do Grafico
    graf_10 = load_img('Assets/Graficos/mundo.png')
    st.image(graf_10)
    
    '''
    ##### Fonte - Banco de dados de uva, vinho e derivados. Embrapa.
    ##### Fonte Indireta - CACEX e DECEX/C.T.I.C..

    ## Análise: 
    
    Pelo gráfico, podemos notar que a maioria dos países do top 10 exportações ficam no hemisfério norte, sendo os maiores consumidores a Europa/Asia (Rússia) e a América do Sul (Paraguai).
    
    '''
    st.divider()
    '''

    ## Conclusão:

    Pela análise, podemos verificar ao longo dos anos uma tendência de crescimento das exportações de vinho em países como a Rússia e o Haiti. Também é possível verificar muito dos grandes consumidores de vinho estão no hemisfério norte, mais especificamente na Europa.
    
    Como estratégia para a empresa em um momento atual, seria interessante focar seus esforços para se adequar ao mercado de vinhos Europeu. Além disso, a empresa deve se preparar para futuramente atender um mercado mais amplo, levando em conta países de outros continentes como o Haiti, Paraguai e China que vem apresentando um aumento em suas demandas pelo produto.
    '''

with tab5:
    '''
    ## Prospecções futuras

    A seguir, podemos verificar pelo gráfico de linhas o valor cumulativo em dólares de exportações futuras simulado para os próximos 5 anos no estado do Rio Grande do Sul.
    
    Utilizamos o cálculo de valor futuro:
    '''
    st.latex(r'''
    VF = VP(1+i) * n
    ''')
    ''' 
    > *onde:  VF = Valor Futuro, VP = Valor Presente, i = Taxa de Crescimento e n = Período em anos.*
    
    Escolhemos 5 diferentes cenários de crescimento nas exportações, sendo eles: crescimento de 0%, 1%, 2%, 3% e 4% nos próximos 5 anos.
    
    A ideia por trás desse gráfico é dar um norte para a empresa de qual será o possível cenário de exportação de vinhos brasileiros do estado do Rio Grande do Sul.
    
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
    
    Podemos concluir que futuramente, como uma estratégia visando o aumento de lucros da empresa, seria interessante em um primeiro momento que a empresa focasse na exportação de seus produtos para países como Rússia, Paraguai e Estados Unidos e países de maior consumo de vinho do continente europeu, pois estes aparentemente têm maior interesse na aquisição de vinhos provindos do Brasil.
    
    Além disso, países como a China e Haiti aparentam ter um potencial futuro para grandes importações de vinho brasileiro, conforme pode-se observar um aumento expressivo em suas importações ao longo dos anos.
    
    Em um cenário mais desafiador e de baixo crescimento das exportações, seria interessante que a empresa focasse em mercados mais tradicionais como o mercado de vinhos Europeu (Principalmente a Rússia), pois a chance de se realizar negócios lucrativos com tal mercado é maior em termos históricos.
    
    Já em um cenário de maior crescimento das exportações, seria interessante expandir o leque de clientes da empresa, englobando países de crescente demanda de importação de vinhos como os Estados Unidos, Paraguai, Haiti e a China.
    '''

with tab6:
    '''
    ## Referências
    
    1. Banco de dados de uva, vinho e derivados. In: Dados da Vitivinicultura. [Bento Gonçalves, RS: Embrapa, Uva e Vinho], 2022. Disponível em: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06. Acessado em: 28 de jun. 2023.

    2. Lista de países por população. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o. Acessado em: 28 de jun. 2023.

    3. List of countries by average yearly temperature. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature. Acessado em: 28 de jun. 2023.
    
    4. List of countries by GDP (nominal). In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal). Acessado em: 28 de jun. 2023.

    5. Matemática financeira. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2023. Disponível em: https://pt.wikipedia.org/wiki/Matem%C3%A1tica_financeira. Acessado em: 28 de jun. 2023.
    '''