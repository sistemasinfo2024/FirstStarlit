import streamlit as st

"""

# Starlit Application

"""

st.text("Información Personal")
t_nombre = st.text_input("Nombre: ", autocomplete="Nombre")
t_apellido = st.text_input("Apellido: ", autocomplete="Apellido")

st.text(f'Hola {t_nombre} {t_apellido}')
