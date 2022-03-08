import streamlit as st
import streamlit.components.v1 as components

from typing import Dict
from io import StringIO

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    # """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def carrega_html(file_name,h):
    components.html(file_name, height=h, scrolling=True)

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

    if (i == 0):
        st.write('')
        st.write('**>> Nenhuma anotação encontrada!!!**')
    else:
        st.write('**'+str(i)+' anotação(ões) encontrada(s)!!!**')
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
    color:#dcdcdc;border:1px solid currentcolor;background-color:#044269;}
    .caretN{cursor:default;
    -webkit-user-select:none;/*Safari3.1+*/
    -moz-user-select:none;/*Firefox2+*/
    -ms-user-select:none;/*IE10+*/
    user-select:none;}
    .caretN::before{content:"⊡";color:#dcdcdc;display:inline-block;margin-right:10px;}
    .caret{cursor:pointer;
    -webkit-user-select:none;/*Safari3.1+*/
    -moz-user-select:none;/*Firefox2+*/
    -ms-user-select:none;/*IE10+*/
    user-select:none;}
    .caret::before{content:"⊞";color:#dcdcdc;display:inline-block;margin-left:10px;margin-right:10px;}
    .caret-down::before{content:"⊟";color:#dcdcdc;display:inline-block;margin-right:10px;}
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
    global static_store
    global html_treeview

    st.set_page_config(
      page_title="APP.io", 
      page_icon="⚙️", 
      layout="centered", # centered/wide
      initial_sidebar_state = "collapsed", # auto/expanded/collapsed
    )
    
    hide_streamlit_style = \
        '''
            <style>
            .css-fg4pbf {background: rgb(242, 242, 242) none repeat scroll 0% 0%;}
            .css-ffhzg2 {background: rgb(61, 70, 87) none repeat scroll 0% 0%;}
            .css-1cpxqw2 {background-color: rgb(185, 213, 206);
                          border: 1px solid rgba(49, 51, 63, 0.2);}
            .css-1cpxqw2:hover {border-color: rgb(16, 134, 114);
                                color: rgb(16, 134, 114);}
            .css-1cpxqw2:focus:not(:active) {border-color: rgb(16, 134, 114);
                                            color: rgb(16, 134, 114);}
            .css-1cpxqw2:focus {box-shadow: rgba(6, 134, 114, 0.18) 0px 0px 0px 0.2rem;
                                outline: currentcolor none medium;}
            .css-1cpxqw2:active {color: rgb(185, 213, 206);
                                 border-color: rgba(0, 0, 0, 0.31);
                                 background-color: rgb(113, 113, 113);}
            .css-1fcdlhc .streamlit-expanderHeader:hover svg {fill: rgb(157, 181, 177);}
            
            .css-po3vlj {background-color: rgb(255, 255, 255); box-shadow: rgb(203, 204, 206) 0px 0px 0px 1px; padding: 0.5rem;}
            .css-po3vlj:focus {box-shadow: rgb(157, 181, 177) 0px 0px 0px 1px;}
            .css-paap06-EmotionIconBase {color: rgb(99, 106, 120);}

            .css-12oz5g7 {padding: 2rem 1rem 10rem;}
            .viewerBadge_container__1QSob {visibility:hidden;}
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        '''
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("🔎 Privacy Finder")
    st.text("Find data privacy requirements.")

    tagBusca = False
    with st.form(key="pydantic_form"):
        st.subheader("🗃️ STEP 1: Carregar Repositório")
        
        html_treeview = '''
        '''

        static_store = get_static_store()
        static_storeA = static_store.copy()
        
        results = st.file_uploader('Load Repository', type='yaml', accept_multiple_files=True)
        if results is not None:
            # Process you file here
            for result in results:
              value = StringIO(result.getvalue().decode("utf-8"))
              # And add it to the static_store if not already in
              if not value in static_store.values():
                  static_store[result.name] = value
        else:
            # Hack to clear list if the user clears the cache and reloads the page
            static_store.clear()  
            st.info("Upload one or more files.")
        
        st.write('')
        
        if static_store:
            st.form_submit_button(label="Load", help=None, on_click=None, args=None, kwargs=None)
            st.write('')
            if (results == []): static_store.clear()
            tagBusca = True
        else: 
            st.form_submit_button(label="Load", help=None, on_click=None, args=None, kwargs=None)
            st.write('')
            if (results == []): static_store.clear()
            tagBusca = False
    
    if tagBusca:
        with st.form(key="find_form"):
            st.subheader("🔍 STEP 2: Buscar")
            st.text("Lista os Requisitos de Privacidade de Dados na API.")
            menuApp = ['...','ALL - Carrega todas as Anotações da API', 
                      'CONCEITO - Busca as Anotações da API por Conceitos',
                      'VIEW - Vizualiza a(s) API(s) carregadas']
            opApp = st.selectbox('Escolha uma Opção:', menuApp, index=0)
            if ('...' in opApp):
                st.form_submit_button(label="OK", help=None, on_click=None, args=None, kwargs=None)
            elif ('ALL' in opApp):
                st.write('___')
                if st.form_submit_button(label="OK", help=None, on_click=None, args=None, kwargs=None):
                  for fl in static_store.keys():
                      with st.expander(('📄 '+fl)):
                          html_treeview = processa(fl)
                          h = len(html_treeview)
                          if (h > 1400): 
                              h=300
                              carrega_html(html_treeview,h)
                          st.write('___')
            elif ('CONCEITO' in opApp):
                st.write('___')
                busca = st.text_input('Buscar por:', '')
                if st.form_submit_button(label="Buscar", help=None, on_click=None, args=None, kwargs=None):
                    st.write('___')
                    st.text('Resultado:')
                    if (busca != ''):
                      st.write('OK')
            elif ('VIEW' in opApp):
                st.write('___')
                if st.form_submit_button(label="OK", help=None, on_click=None, args=None, kwargs=None):
                    st.write('')
                    for fl in static_storeA.keys():
                        with st.expander(fl):
                            strIO = static_storeA.get(fl)
                            string_data = strIO.read()
                            st.write('')
                            st.code(string_data, language='yaml')
                            st.write('')
  
if __name__ == '__main__':
   main()
