import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="APP.io", 
    page_icon="⚙️", 
    layout="wide", # centered/wide
    initial_sidebar_state = "expanded", # auto/expanded/collapsed
)


def local_html(file_name):
    with open(file_name) as f1:
        components.html(f1.read(), height=800, scrolling=True)

def home():
    sm_li = """<a href='https://www.linkedin.com/in/dorneliomori/' target="_blank"><i class=" fa fa-linkedin-square" style="font-size:48px;color:blue"></i></a>"""
    sm_gg = """<a href='mailto:dmj.tanaka@gmail.com' target="_blank"><i class="fa fa-google-plus-square" style="font-size:48px;color:red"></i></a>"""
    sm_gh = """<a href='https://github.com/TNK443/Streamit/' target="_blank"><i class="fa fa-github-square" style="font-size:48px;color:black"></i></a>"""
    sm_ifesSerra = """<a href='https://www.ifes.edu.br/cursos/pos-graduacao/mestrado-em-computacao-aplicada' target="_blank"><img src='https://www.ifes.edu.br/templates/padraogoverno01/favicon-32x32.png'></a>"""
    sm_ifesColatina = """<a href='https://www.ifes.edu.br/cursos/pos-graduacao/pos-graduacao-lato-sensu-em-conectividade-e-tecnologias-da-informacao' target="_blank"><img src='https://www.ifes.edu.br/templates/padraogoverno01/favicon-32x32.png'></a>"""

    # st.write('___')
    # st.title('Uso de Anotação Semântica para identificação de requisitos de Privacidade de Dados em Serviços Web', anchor='titulo')
    # st.write('___')
    st.subheader('Autores:', anchor='autores')
    st.write('###### - MORI JR., Dornélio')
    st.write('[ IFES-Serra | Serra, ES - Brasil | dmj.tanaka@gmail.com ]')
    st.write('###### - NARDI, Julio Cesar')
    st.write(f'[ IFES-Colatina | Colatina, ES - Brasil | julionardi@ifes.edu.br ] {sm_ifesColatina}', unsafe_allow_html=True)
    st.write('###### - RUY, Fabiano Borges')
    st.write(f'[ IFES-Serra | Serra, ES - Brasil | fabianoruy@ifes.edu.br ] {sm_ifesSerra}', unsafe_allow_html=True)    

    st.write('___')
    st.header('Introdução', anchor='intro')
    st.write('Introdução do Artigo.')
    st.write('Introdução do Artigo.')

    st.write('___')
    st.header('Seções', anchor='sec')
    st.write('**Home:** Informações sobre o Trabalho.')
    st.write('**Aplicação:** Informações da Aplicação/Protótipo.')
    st.write('**Ontologia:** Ontologia sobre Privacidade de Dados Pessoais.')
    st.write('**Outras Informações:** ....')

    st.write('___')
    st.header('Contato', anchor='contato')
    st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    st.write(f'{sm_li}  {sm_gg}  {sm_gh}', unsafe_allow_html=True)

    st.write('___')
    st.subheader('Source Code, Bugs, Feature Requests', anchor='source')
    githublink = """<a href='https://github.com/TNK443/Streamit' target="_blank">https://github.com/TNK443/Streamit</a>"""
    st.write(f'\n\nCheck out the GitHub Repo at: {githublink}. If you find any bugs or have suggestions, please open a new issue and I will look into it.', unsafe_allow_html=True)
    st.write('___')


def app():
  menuApp = ['Busca', 'Busca OPENAPI']
  options = st.selectbox('Função:', menuApp)
  local_html("HTML")


def main():
    st.write('___')
    st.title('Uso de Anotação Semântica para identificação de requisitos de Privacidade de Dados em Serviços Web', anchor='titulo')
    st.write('___')

    st.sidebar.write('___')
    st.sidebar.title('Uso de Anotação Semântica para identificação de requisitos de Privacidade de Dados em Serviços Web')
    st.sidebar.caption('(MORI JR, Dornelio; NARDI, Julio Cesarl; RUY, Fabiano Borges)')
    st.sidebar.write('___')

    # Sidebar Navigation
    menu = ['Home', 'Aplicação', 'Ontologia', '...']
    options = st.sidebar.selectbox('',menu)
    if options == 'Home':
       home()
    elif options == 'Aplicação':
      app()
    else:
       pass


if __name__ == '__main__':
   main()