import streamlit as st
import about
import basics
import home
import otros
import ambiente_pred


PAGES = {
	"Home": home,
	"Elementos Básicos": basics,
	"Otros Elementos":otros,
	"Ambiente Predictivo": ambiente_pred,
	"Página Final": about,
}


def main():
	"""Main function of the App"""
	st.sidebar.title("Navegación")
	selection = st.sidebar.radio("Ir a", list(PAGES.keys()))

	page = PAGES[selection]
	#with st.spinner(f"Cargando {selection} ..."):
	page.write()

	st.sidebar.title("Diseño")
	st.sidebar.info(
        """Esta página fue construída por [LHLAB](https://lhlab.cl/) para el [PyDay Chile 2020](https://pyday.cl/) con herramientas Open Source. Streamlit es un proyecto open source y se puede visitar su página web 
         [aquí](https://www.streamlit.io/) y también su github puede ser vistado en el siguiente [link]()""")
        # 	st.sidebar.title("Acerca de")



if __name__ == "__main__":
	main()
