import streamlit as st
import streamlit.components.v1 as components
import streamlit_pydantic as sp

from streamlit_pydantic.types import FileContent
from pydantic import BaseModel, Field
from typing import Optional, List
from io import StringIO

class ExampleModel(BaseModel):
    load_repository: Optional[List[FileContent]] = Field(
        None,
        description="Carregue (Upload) o Repositório de API's OpenAPI v3 ( .yaml ). ",
        st_kwargs_type=["yaml"],
    )

def carrega_html(file_name,h):
    components.html(file_name, height=h, scrolling=True)


def main():
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
        data = sp.pydantic_input(key="my_form", model=ExampleModel)
        # st.write('___')
        if data["load_repository"]!=[]:
            st.form_submit_button(label="View Repository", help=None, on_click=None, args=None, kwargs=None)
            for _ in data["load_repository"]:
                with st.expander(""):
                    string_data = StringIO(_.decode("utf-8")).read()
                    st.write('')
                    st.code(string_data, language='yaml')
                    st.write('')
            tagBusca = True
        else: 
            st.form_submit_button(label="View Repository", help=None, on_click=None, args=None, kwargs=None)
            st.write('')
    

    if tagBusca:
        with st.form(key="find_form"):
            st.subheader("🔍 STEP 2: Buscar")
            st.text("Lista os Requisitos de Privacidade de Dados na API.")

            menuApp = ['...','ALL - Carrega todas as Anotações da API', 
                      'CONCEITO - Busca as Anotações da API por Conceitos']
            opApp = st.selectbox('Escolha uma Opção:', menuApp, index=0)
            st.form_submit_button(label="OK", help=None, on_click=None, args=None, kwargs=None)
        
if __name__ == '__main__':
   main()
