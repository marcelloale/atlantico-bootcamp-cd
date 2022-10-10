#instalar as bibliotecas
#poetry add streamlit
#poetry add scikit-learn
#poetry add matplotlib
#poetry add pandas

#importando as bibliotecas
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#titulo
st.title("Aprendendo a usar o streamlit")

#ler dataset
df = pd.read_csv("data/raw/datarich.csv")

#ver dataset
#st.line_chart(df)
st.dataframe(df)

#cabeçalho
st.subheader("Informações dos dados")

#recebendo o nomedousuário
user_input = st.sidebar.text_input("Digite seu nome")

#printando o nome do usuário
st.write("Olá ", user_input)

#dados de entrada
# x = sem a coluna resultado(default) 
#x = df.drop(['default.payment.next.month'],1)
#y = df['default.payment.next.month']

#separa dados em treinamento e teste
#x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2)

#dados dos usuários como função
def get_user_date():
    idade = st.sidebar.slider ("IDADE", 21, 79, 34)
    estado= st.sidebar.radio ("ESTADO CIVIL", ("Solteiro","Casado","Outros"))
    sexo  = st.sidebar.selectbox ("SEXO", ("feminino", "masculino"), key='sexo')
    educa = st.sidebar.slider ("ESCOLARIDADE", 0, 6, 1)
    limit = st.sidebar.number_input("Limite do seu cartão de crédito", min_value=0.0, step=100.0, key='limit')

    #dicionário para receber informações
    user_data = {'Idade': idade,
             'Estado Civil': estado,
             'Sexo': sexo,
             'Escolaridade': educa,
             'Limite de Credito': limit
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

user_input_variables = get_user_date()

#markdown
st.write("""
## Risk Prediction
Dataset de *Taiwan*
"""
)


#grafico
#graf = st.bar_chart(user_input_variables)

#escolher cor
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

if st.button("Pronto!"):
    st.balloons()