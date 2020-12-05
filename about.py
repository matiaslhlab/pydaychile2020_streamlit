"""Home page shown when the user enters the application"""
import streamlit as st
from PIL import Image

def write():
	image_lhlab = Image.open(r'resources/lhlab_claro.png')
	image_pyday = Image.open(r'resources/PyDayLogo.png')
	#st.image(image_lhlab,width=420)
	st.title("Página Final")
	st.markdown(
"""
## Agradecimientos

Queremos agradecer la invitación al equipo organizador que nos extendieron a este evento PyDay Chile 2020.

También pueden visitarnos en nuestra página web: [lhlab.cl](https://lhlab.cl/) y en su perfil de [linkedin](https://www.linkedin.com/company/33231607).
""", unsafe_allow_html=True,
        )

	image_web = Image.open(r'resources/lhlab_webpage.png')
	st.image(image_web, caption='¡Los esperamos!',use_column_width=True)
	celebrar=st.button('Terminar charla PyDay Chile 2020')
	if celebrar:
		st.balloons()
