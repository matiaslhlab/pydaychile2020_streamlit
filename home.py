"""Home page shown when the user enters the application"""
import streamlit as st
from PIL import Image

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Cargando Home ..."):
        st.title('LHLAB: Maqueta de uso de Streamlit')
        st.write(
            """
Ahora que ya vimos las principales caracteríticas de Streamlit, esta aplicación pretende hacer una demostración rapida de los principales elementos desarrollados en Streamlit hasta la fecha.
Dentro de este paseo guiado podremos visitar:
- Un **compendio o zoología** de los elementos básicos que presenta la herramienta
- Un par de **elementos extra** que pueden enriquecer aún las la experiencia y la integración con el usuario
- Finalmente una aplicación simple de un **ambiente predictivo** donde se puede entrenar un conjunto de modelos para ver su desempeño a partir de un dataset determinado.""")


        st.header("Recursos y ayudas utilizadas")
        st.write("""
Para desarrollar esta aplicación se usaron algunos recursos de la web, los cuales compartiremos a continuación para que puedan ser consultados:
- [Documentación Oficial de Streamlit](https://docs.streamlit.io/en/stable/)
- [Interfaz de usuario para Deepstack (github)](https://github.com/robmarkcole/deepstack-ui)
- [Dataset de prueba para ambiente predictivo](https://www.kaggle.com/uciml/indian-liver-patient-records)
- [D-TALE, aplicacion para dataframes de Pandas](https://github.com/man-group/dtale)
""")
        image=Image.open(r'resources/lhlab_claro.png')
        st.image(image,width=540)
