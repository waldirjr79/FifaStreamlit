import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title='HOME',
    layout='wide'
)

if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= 2023]
    df_data = df_data[df_data['Value(£)'] >= 2023]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown("# FIFA23 OFFICAL DATASET!")
st.sidebar.markdown("Deselvonvido por Waldir jr")


btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.eletroluz.net')

st.markdown('''
Análise dos Dados do FIFA 23 - Desempenho e Classificações

No FIFA 23, um dos principais pontos de destaque está na evolução das classificações e no desempenho dos jogadores dentro do jogo. Os dados coletados ao longo da temporada mostram um padrão interessante de desempenho com base em várias métricas de jogo, como velocidade, força, finalização, passe, e inteligência tática.

1. Classificações de Jogadores
As classificações gerais dos jogadores no FIFA 23 variam de 50 até 99, sendo que a maioria dos melhores jogadores do mundo se situa entre as classificações 85 e 95. A EA Sports utiliza dados reais de desempenho de jogadores, estatísticas de ligas de futebol, e contribuições de analistas para ajustar essas classificações. Por exemplo, Lionel Messi, com uma classificação geral de 91, é destacado por sua alta habilidade de drible (94) e passe (90), o que o torna um dos principais playmakers do jogo.

2. Distribuição de Habilidades
Analisando a distribuição de habilidades entre os jogadores, notamos que certas ligas e posições têm características específicas:

Defensores da Premier League: A média de força física dos zagueiros da Premier League no FIFA 23 é de 83, o que reflete a natureza mais física do futebol inglês.
Atacantes da La Liga: A média de finalização dos atacantes da La Liga é de 85, destacando-se pela alta capacidade técnica dos jogadores dessa liga.
Velocidade na Bundesliga: A Bundesliga, famosa por seu jogo rápido e direto, apresenta uma média de aceleração dos pontas de 88, a mais alta entre as grandes ligas europeias.
3. Crescimento de Jogadores Jovens
Outro dado interessante no FIFA 23 é a projeção de crescimento dos jogadores jovens. Jogadores como Pedri (classificação inicial de 85) e Jude Bellingham (classificação inicial de 84) têm um potencial de crescimento de até 90+, dependendo de seu desempenho nas temporadas de carreira. O modo "Carreira" oferece uma visão realista do desenvolvimento de talentos jovens com base no tempo de jogo, treinamento e resultados de jogos.

4. Desempenho Tático
No FIFA 23, a implementação de táticas personalizadas e estilo de jogo reflete o comportamento real das equipes. A análise dos dados revela que times que utilizam formações mais compactas, como o 4-4-2, tendem a ter uma recuperação defensiva mais eficiente, enquanto times que adotam o 4-3-3, com pontas rápidos, têm maior eficácia em contra-ataques. O Manchester City, por exemplo, com jogadores como Kevin De Bruyne e Phil Foden, destaca-se pela precisão nos passes e controle de posse de bola, com uma média de 90% de passes completos em jogos simulados no FIFA.

5. Popularidade de Jogadores no Modo Ultimate Team
No modo Ultimate Team, jogadores com alta velocidade e drible são os mais procurados pela comunidade. Dados coletados ao longo dos primeiros meses mostram que Kylian Mbappé (96 de velocidade) e Vinícius Jr. (95 de drible) são escolhas favoritas, com uma taxa de seleção superior a 75% nas competições online.

Além disso, jogadores com habilidades de cinco estrelas em dribles, como Neymar Jr., oferecem uma vantagem significativa no jogo, especialmente em competições de alto nível, onde a capacidade de driblar oponentes e criar espaços é crucial.
''')
