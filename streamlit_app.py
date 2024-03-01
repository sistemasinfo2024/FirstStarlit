import streamlit as st
import pandas as pd


st.title("First Stalit Application")
st.text("Información Personal")
t_nombre = st.text_input("Nombre: ", autocomplete="Nombre")
t_apellido = st.text_input("Apellido: ", autocomplete="Apellido")

"""

### Los datos del dataset de salud

"""

# data = pd.DataFrame([[t_nombre, t_apellido]], columns=['Nombre', 'Apellido'])
data = pd.read_excel('https://github.com/roscha10/ProyectoM6_machine_learning/raw/main/Propuesta%201/BBDD_Hospitalizaci%C3%B3n.xlsx')

st.dataframe(data)
