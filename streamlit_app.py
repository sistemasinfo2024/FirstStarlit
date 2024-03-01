import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
"""

# Primer App Starlit

Aplicaciones de negocio implementadas en Streamlit

"""

data = pd.read_excel('https://github.com/roscha10/ProyectoM6_machine_learning/raw/main/Propuesta%201/BBDD_Hospitalizaci%C3%B3n.xlsx')

print(data)

st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True
