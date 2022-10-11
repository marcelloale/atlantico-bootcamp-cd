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

#markdown
st.write("""
## Prevendo Diabetes
Dataset do **Instituto Nacional de Diabetes e Doenças Digestivas e Renais**, *India*
"""
)
#fonte https://medium.com/data-hackers/desenvolvimento-de-um-aplicativo-web-utilizando-python-e-streamlit-b929888456a5
#ler dataset
df = pd.read_csv("data/raw/diabetes.csv")

#ver dataset
st.dataframe(df)
#st.line_chart(df)

#cabeçalho
st.subheader("Informações dos dados")

#recebendo o nomedousuário
user_input = st.sidebar.text_input("Digite seu nome")

#printando o nome do usuário
st.write("Olá ", user_input)

#dados de entrada
# x = sem a coluna resultado(default) 
x = df.drop(['Outcome'],1)
y = df['Outcome']

#separa dados em treinamento e teste 20%
x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2)

# .slider .radio .selectbox .numberinput
#dados dos usuários como função
def get_user_date():
    # 
    pregnancies = st.sidebar.slider("Gravidez",0, 15, 1)
    glicose = st.sidebar.slider("Glicose", 0, 200, 110)
    blood_pressure = st.sidebar.slider("Pressão Sanguínea", 0, 122, 72)
    skin_thickness = st.sidebar.slider("Espessura da pele", 0, 99, 20)
    insulin = st.sidebar.slider("Insulina", 0, 900, 30)
    bni= st.sidebar.slider("Índice de massa corporal", 0.0, 70.0, 15.0)
    dpf = st.sidebar.slider("Histórico familiar de diabetes", 0.0, 3.0, 0.0)
    age = st.sidebar.slider ("Idade", 15, 100, 21)

    #dicionário para receber informações
    user_data = {"Gravidez": pregnancies,
                "Glicose": glicose,
                "Pressão Sanguínea": blood_pressure,
                "Espessura da pele": skin_thickness,
                "Insulina": insulin,
                "Índice de massa corporal": bni,
                "Histórico familiar de diabetes": dpf,
                "Idade": age
                }

    features = pd.DataFrame(user_data, index=[0])
    return features

user_input_variables = get_user_date()

#grafico
graf = st.bar_chart(user_input_variables)
dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dtc.fit(x_train, y_train)

#acurácia do modelo
st.subheader('Acurácia do modelo')
st.write(accuracy_score(y_test, dtc.predict(x_text)))

#previsão do resultado
prediction = dtc.predict(user_input_variables)
st.subheader('Previsão:')
st.write(prediction)




#escolher cor
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

if st.button("Pronto!"):
    st.balloons()
    
