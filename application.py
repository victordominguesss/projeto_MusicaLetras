import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response = requests.get(endpoint)
    letra = response.json()['lyrics'] if response.status_code == 200 else ''
    return letra


st.image('img/istockphoto-1391884768-612x612.jpg')
st.title('Letras de músicas')

banda = st.text_input('Digite o nome da banda/cantor(a): ', key='banda')
musica = st.text_input('Digite o nome da música: ', key='musica')
pesquisar = st.button('Pesquisar')

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success('Letra encontrada!')
        st.text(letra)
    else:
        st.error('Infelizmente encontramos a letra desta música')
