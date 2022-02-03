import streamlit as st

import pandas as pd
import numpy as np #gerando um dataframe aleatório
import time
from random import randint

df = pd.DataFrame(
    np.random.randn(15,10),
    columns=('col_%d' % i for i in range(10))
 )#tabelas interativas

st.set_page_config(
    page_title="Teste.io", 
    page_icon="⚙️", 
    layout="wide", # centered/wide
    initial_sidebar_state = "collapsed", # auto/expanded/collapsed
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
    }
  
  )

def main():
  with st.spinner('Wait for it...'):
    time.sleep(5)
  st.success('Done! \n') 
  
  st.title("Streamlit - Title")
  st.header("Stramlit - Header")
  st.subheader("Streamlit - Subheader")
  st.text("Streamlit - Text")

  #formatação
  st.markdown('Texto em **negrito** ou _itálico_')#Utilização para guardar html
  st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)',False)

  st.dataframe(df)#tabelas fixas
  st.table(df)

  menu = ["Home", "Teste", "About"]
  choice = st.sidebar.selectbox('Menu', menu)
  if choice == 'Teste':
      st.subheader("Streamlit - Subheader - Teste")



  #Botão
  if st.button('Gerar número aleatório'):
    st.write(randint(0, 1000000))
  else:
    st.write('Clique no botão acima')
    
  #Radio
  chute = st.radio(
      "por que essa função se chama radio?",
      ('Opção 1: porque o rádio é um osso muito bonito',
      'Opção 2: é uma homenagem à Marie Curie',
      'Opção 3: as opções lembram botões de rádio')
  )
  
  if chute == 'as opções lembram botões de rádio':
      st.write('Correto!')
  else:
      st.write("Incorreto, tente novamente.")



  #Barra de arraste
  bar = st.slider('Isso é um slider',
      min_value=0,
      max_value=10,
      value=5,
      step=1)
  st.write("você selecionou: ",bar)



  #caixa de multiseleção
  #obs.: utilizando o dataframe criado anteriormente
  cx_mult = st.multiselect(
      'Selecione as colunas abaixos',
      df.columns
  )
  st.table(df[cx_mult])
  st.write(df[cx_mult])





  #input de números
  input_num = st.number_input(
        'Escreva um número entre 0 e 10',
        min_value = 0,
        max_value = 10,
        value = 0,
        step = 1
  )
  st.write('O número inputado foi: ', input_num)
  
  #input de texto
  input_txt = st.text_input(
        'Escreva uma palavra com até 5 letras',
        value = 'juiz',
        max_chars = 5
  )
  st.write('A palavra inputada foi: ', input_txt)
















if __name__ == '__main__':
  main()

# st.write("# Hello!")
# st.write("## Run exemplo.")