import streamlit as st
import streamlit.components.v1 as components

from typing import Dict
from io import StringIO

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    # """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def upload_arq():
    # """Run this function to run the app"""
    global static_store
    static_store = get_static_store()

    st.sidebar.write('**Carregar arquivo(s) OPENAPI v3:**')
    results = st.sidebar.file_uploader('Upload', type='yaml', accept_multiple_files=True)
    if results is not None:
        # Process you file here
        for result in results:
          value = StringIO(result.getvalue().decode("utf-8"))

          # And add it to the static_store if not already in
          if not value in static_store.values():
              static_store[result.name] = value
    else:
        static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
        st.sidebar.info("Upload one or more files.")

    if st.sidebar.button("Clear file list"):
        static_store.clear()
    
    st.sidebar.write('')
    st.sidebar.write('')
    if st.sidebar.checkbox("Show file list?", True):
        for _ in static_store.keys():
          st.sidebar.write(' - '+_)

def home():
    sm_li = """<a href='https://www.linkedin.com/in/dorneliomori/' target="_blank"><i class=" fa fa-linkedin-square" style="font-size:48px;color:blue"></i></a>"""
    sm_gg = """<a href='mailto:dmj.tanaka@gmail.com' target="_blank"><i class="fa fa-google-plus-square" style="font-size:48px;color:red"></i></a>"""
    sm_gh = """<a href='https://github.com/TNK443/Streamit/' target="_blank"><i class="fa fa-github-square" style="font-size:48px;color:black"></i></a>"""
    sm_ifesSerra = """<a href='https://www.ifes.edu.br/cursos/pos-graduacao/mestrado-em-computacao-aplicada' target="_blank"><img src='https://www.ifes.edu.br/templates/padraogoverno01/favicon-32x32.png'></a>"""
    sm_ifesColatina = """<a href='https://www.ifes.edu.br/cursos/pos-graduacao/pos-graduacao-lato-sensu-em-conectividade-e-tecnologias-da-informacao' target="_blank"><img src='https://www.ifes.edu.br/templates/padraogoverno01/favicon-32x32.png'></a>"""

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

def carrega_html(file_name, h):
    components.html(file_name, height=h, scrolling=True)

def aplicacao():
    global static_store
    global html_treeview

    html_treeview = '''
    '''

    st.sidebar.write('___')
    upload_arq()
    
    st.write('## **Anotação Semântica OPENAPI v3:** descrimina os Requisitos de Privacidade de Dados na API.')
    menuApp = ['...','ALL - Carrega todas as Anotações da API', 
               'CONCEITO - Busca as Anotações da API por Conceitos',
               'VIEW - Vizualiza a(s) API(s) carregadas']
    opApp = st.selectbox('Escolha uma Opção:', menuApp, index=0)
    if ('ALL' in opApp):
        st.write('___')
        if st.button("Carregar TreeView"):
           for fl in static_store.keys():
              with st.expander(fl):
                  st.write('## ARQUIVO: '+fl)
                  html_treeview = processa(fl)
                  h = len(html_treeview)
                  if (h > 1271): 
                      st.write(h)
                      h=500
                      carrega_html(html_treeview,h)
                  st.write('___')

    elif ('CONCEITO' in opApp):
        st.write('___')
        busca = st.text_input('Buscar por:', '')
        if (busca != ''):
          st.write('OK')

    elif ('VIEW' in opApp):
        st.write('___')
        st.write('')
        for fl in static_store.keys():
            with st.expander(fl):
                strIO = static_store.get(fl)
                string_data = strIO.read()
                st.write('')
                st.code(string_data, language='yaml')
                st.write('')


def processa(fileproc): 
# ----------------------------------------------------------------------------------------------------
# Trabalhando os Arquivos como TEXTO - GERANDO HTML
# ----------------------------------------------------------------------------------------------------
    global static_store
    global html_treeview

    lnCount = 0
    i = 0
    aux = ''
    auxLHierarquia = []
    auxPHierarquia = []

    extensaoOAS = ['x-refersTo','x-kindOf','x-mapsTo','x-collectionOn','x-onResource','x-operationType']

    stringio = static_store.get(fileproc)
    lines = stringio.readlines()
    for ln in range(len(lines)):
        lnCount+=1
        line = lines[ln]
        for chr in line:
          if (aux == '- '): aux=''
          if (aux == '  '):
              i+=1
              aux=''
          if (chr == '\n'):
              if (aux!=''):
                if (i<=9): auxLHierarquia.append('0'+str(i)+aux+' (line '+str(lnCount)+')')
                else: auxLHierarquia.append(str(i)+aux+' (line '+str(lnCount)+')')
              i=0
              aux = ''
              continue
          aux += chr
    # --------------------------------------------------------
    aux = auxLHierarquia.copy()
    aux.reverse()
    for _ in aux: auxPHierarquia.append(_)
    # --------------------------------------------------------
    i,x=0,0
    caminhoCompleto=''

    htmlA='<li><span class="caret">'
    htmlB='</span><ul class="nested">'
    htmlC='</ul></li>'
    htmlD='<li><span class="caretN">'
    htmlE='</span></li>'
    htmlList=[]

    for ln in aux:
        if (ln.find('x-')>0):
            ln_ = ln.strip()
            ln_ = ln_.split(':')[0]
            if (ln_[2:]) in extensaoOAS:
                i+=1           
                x=(int(ln[:2])-1)
                caminhoCompleto += htmlD
                caminhoCompleto += ln[2:]
                caminhoCompleto += htmlE
                for j in auxPHierarquia:
                    if (int(j[:2]) == x):
                        caminhoCompleto = htmlA + j[2:] + htmlB + '\n' + caminhoCompleto #+ htmlC
                        if (x==0): break
                        else: x-=1
                htmlList.append(caminhoCompleto)
                caminhoCompleto=''
        auxPHierarquia.pop(0)

    print()
    st.write('')
    if (i == 0):
        print('>> Nenhuma anotação encontrada!!!')
        st.write('>> Nenhuma anotação encontrada!!!')
    else:
        print(i, 'anotação(ões) encontrada(s)!!!')
        st.write(i, 'anotação(ões) encontrada(s)!!!')
    print('-'*60)
    print()
    st.write('')
    # --------------------------------------------------------
    htmlListFull=[]
    A,B,B_=[],[],[]

    htmlList.reverse()
    for ln in htmlList:
        if (htmlListFull!=[]):
            i=0
            j = len(A)-1
            B = ln.split('\n')
            B_= ln.split('\n')
            while 1:
                  if (A[i]==B[i]):
                      j-=1
                      B_.pop(0)
                  else:
                      htmlListFull.extend((j*htmlC).split())
                      htmlListFull.extend(B_)
                      A = ln.split('\n')
                      break
                  i+=1             
        else:
            htmlListFull = ln.split('\n')

            A = ln.split('\n')

    j = len(ln.split('\n'))-1
    htmlListFull.extend((j*htmlC).split())
    
    html_treeview = '''
    <ul id="myUL"><p></p>
    '''

    for ln in htmlListFull: html_treeview += ln


    html_treeview += '''
    <p></p></ul>
    <style>
    ul,#myUL{list-style-type:none;}
    #myUL{margin:0;padding:0;
    color:#044269;border:2px solid currentcolor;background-color:#DCDCDC;}
    .caretN{cursor:default;
    -webkit-user-select:none;/*Safari3.1+*/
    -moz-user-select:none;/*Firefox2+*/
    -ms-user-select:none;/*IE10+*/
    user-select:none;}
    .caretN::before{content:"⊡";color:grey;display:inline-block;margin-right:10px;}
    .caret{cursor:pointer;
    -webkit-user-select:none;/*Safari3.1+*/
    -moz-user-select:none;/*Firefox2+*/
    -ms-user-select:none;/*IE10+*/
    user-select:none;}
    .caret::before{content:"⊞";color:black;display:inline-block;margin-right:10px;}
    .caret-down::before{content:"⊟";color:grey;display:inline-block;margin-right:10px;}
    .nested{display:none;}
    .active{display:block;}
    </style>

    <script>
    var toggler = document.getElementsByClassName("caret");
    var toggler1 = document.getElementsByClassName("caretN");
    var i;

    for (i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function() {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("caret-down");
      });
    }
    </script>
    '''

    return html_treeview
    # --------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------


def main():   
    # Configurações inciais
    st.set_page_config(
      page_title='APP.io', 
      page_icon='⚙️', 
      layout='wide', # centered/wide
      initial_sidebar_state = 'collapsed' # auto/expanded/collapsed
    )

    hide_streamlit_style = \
        '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        '''
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Disable Warnings
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # CABECALHO_PRINCIAL_TITULO
    st.write('___')
    st.title('Uso de Anotação Semântica para identificação de requisitos de Privacidade de Dados em Serviços Web', anchor='titulo')
    st.write('___')
    
    # SIDEBAR
    st.sidebar.write('___')
    st.sidebar.write('## Uso de Anotação Semântica para identificação de requisitos de Privacidade de Dados em Serviços Web')
    st.sidebar.caption('(MORI JR, Dornelio - NARDI, Julio Cesarl - RUY, Fabiano Borges)')
    st.sidebar.write('___')

    menu = ['Home', 'Aplicação', 'Ontologia', '...']
    options = st.sidebar.selectbox('Select View', menu)
    if options == 'Home':
       home()
    elif options == 'Aplicação':
       aplicacao()
    else:
       pass


if __name__ == '__main__':
   main()
