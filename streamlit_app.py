import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def showPie(columna):
  count_values = pd.Series(columna).value_counts()
  datos = pd.DataFrame({"valor":count_values.index, "ocurrencia": count_values.values})

  plt.title(columna.name)
  plt.pie(datos["ocurrencia"], labels=datos['valor'], autopct='%1.1f%%')
  plt.show()

st.title("First Stalit Application")
st.text("Información Personal")
t_nombre = st.text_input("Nombre: ", autocomplete="Nombre")
t_apellido = st.text_input("Apellido: ", autocomplete="Apellido")

"""

### Los datos del dataset de salud

"""

# data = pd.DataFrame([[t_nombre, t_apellido]], columns=['Nombre', 'Apellido'])
data = pd.read_excel('https://github.com/roscha10/ProyectoM6_machine_learning/raw/main/Propuesta%201/BBDD_Hospitalizaci%C3%B3n.xlsx')

sns.histplot(data['EDAD'])
