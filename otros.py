import streamlit as st
import dtale 
from dtale.views import startup
import numpy as np
import pandas as pd

def write():
	with st.spinner("Cargando Otros Elementos ..."):
		st.title("Otros elementos de Streamlit")
	st.header("Reportes en PowerBI")
	
	url1="https://app.powerbi.com/view?r=eyJrIjoiMDA4NGFhNmEtZDE4Mi00MWNhLTg5OTMtMWE2MzYxNTVmMTFlIiwidCI6ImI3M2IxZDZlLTIxZDUtNGUzOC1iMjM5LTgxMzRkOWQyYmY3OCIsImMiOjh9"
	st.subheader("Podemos integrar un reporte realizado en PowerBI (de 800x540)")	
	st.markdown('''
 	<iframe width="840" height="540" src="%s" frameborder="0" style="border:0" allowfullscreen="true"></iframe>
	''' % url1, unsafe_allow_html=True)
	st.write("código:")
	st.code("""url1="https://app.powerbi.com/view?r=eyJrIjoiMDA4NGFhNmEtZDE4Mi00MWNhLTg5OTMtMWE2MzYxNTVmMTFlIiwidCI6ImI3M2IxZDZlLTIxZDUtNGUzOC1iMjM5LTgxMzRkOWQyYmY3OCIsImMiOjh9"
st.subheader("Podemos tener un reporte de 800x540")	
st.markdown('''
<iframe width="840" height="540" src="%s" frameborder="0" style="border:0" allowfullscreen="true"></iframe>''' % url1, unsafe_allow_html=True)""")

	url2="https://app.powerbi.com/view?r=eyJrIjoiMjEwYjgzNWUtZGQ4Ni00ODMwLWI0NjgtNzk3NjkxODIwNDM4IiwidCI6IjFmZjk0MGQ4LWFkOGEtNDNkZi1iZjQxLWI2OThkMWJkODVmNiIsImMiOjh9"
	st.subheader("O también algo tener el reporte un poco más pequeño (de 560x360)")	
	st.markdown("""
    <iframe width="560" height="360" src="%s" frameborder="0" style="border:0" allowfullscreen="true"></iframe>
    """ % url2, unsafe_allow_html=True)
	st.write("código:")
	st.code('''url2="https://app.powerbi.com/view?r=eyJrIjoiMjEwYjgzNWUtZGQ4Ni00ODMwLWI0NjgtNzk3NjkxODIwNDM4IiwidCI6IjFmZjk0MGQ4LWFkOGEtNDNkZi1iZjQxLWI2OThkMWJkODVmNiIsImMiOjh9"
st.subheader("O también algo más pequeño de 560x360")	
st.markdown("""
<iframe width="560" height="360" src="%s" frameborder="0" style="border:0" allowfullscreen="true"></iframe>""" % url2, unsafe_allow_html=True)''')

	st.header("Dataframes Interactivos en D-TALE")
	st.markdown("""D-Tale es una herramienta Open Source que permite ver, analizar y modificar de una manera fácil estructuras de datos en Pandas. Para más información ver su [github](https://github.com/man-group/dtale)""")
	df=pd.read_csv(r'dataset/indian_liver.csv')
	startup(data_id="1", data=df)
	st.markdown("""<iframe width="840" height="540" src="/dtale/main/1" />""",unsafe_allow_html=True)
	st.write("código:")
	st.code('''st.markdown("""D-Tale es una herramienta Open Source que permite ver, analizar y modificar de una manera fácil estructuras de datos en Pandas. Para más información ver su [github](https://github.com/man-group/dtale)""")
df=pd.read_csv(r'dataset/indian_liver.csv')
startup(data_id="1", data=df)
st.markdown("""<iframe width="840" height="540" src="/dtale/main/1" />""",unsafe_allow_html=True)''')