import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from datetime import time,datetime,date
from io import StringIO
import time as tim
from PIL import Image

def write():
	with st.spinner("Cargando Elementos Básicos ..."):
		st.title("Elementos Básicos de Streamlit")

######################ELEMENTOS DE TEXTO########################################
	st.header("Elementos de Texto")
	with st.beta_expander('Elementos de encabezado'):
		st.title("Esto es un titulo")
		st.code("""st.title("Esto es un titulo")""")
		st.header('Esto es un encabezado')
		st.code("""st.header('Esto es un encabezado')""")
		st.subheader('Esto es un subencabezado')
		st.code("""st.subheader('Esto es un subencabezado')""")

	with st.beta_expander("Elementos de markdown"):
		st.markdown(	
		'''
		# Esto es un título en markdown 
		## Esto es un encabezado
		### Esto es subencabezado

		:+1: :sunglasses: Y esto es una lista:
		- Item 1
		- Item 2

		''')
		st.code("""st.markdown(	
		'''
		# Esto es un título en markdown 
		## Esto es un encabezado
		### Esto es subencabezado

		:+1: :sunglasses: Y esto es una lista:
		- Item 1
		- Item 2

		''')""")

	with st.beta_expander("Elementos de texto simple"):
		st.text('Tenemos un texto de ancho fijo')
		st.code("""st.text('Tenemos un texto de ancho fijo')""")
		st.text('Podemos además insertar listas de objetos:')
		st.write(['st', 'is <', 3])
		st.code("""st.write(['st', 'is <', 3])""")
		st.write("Y podemos tambien insertar ecuaciones de Látex:")
		st.latex(r''' e^{i\pi} + 1 = 0 ''')
		st.code("""st.latex(r''' e^{i\pi} + 1 = 0 ''')""")


######################ELEMENTOS DE DATA########################################
	st.header("Elementos de Data")
	with st.beta_expander("Elementos para mostrar data "):

		st.write("Podemos mostrar la información contenida en un dataframe de Pandas:")
		df = pd.DataFrame(np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
		st.dataframe(df.style.highlight_max(axis=0)) #resaltamos los máximos
		st.code("""df = pd.DataFrame(np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0)) #seteamo el ancho y largo, resaltamos los máximos""")

		st.write("También podemos mostrar la misma información a través de una tabla simple:")
		st.table(df.iloc[0:10])
		st.code("""st.table(df.iloc[0:10])""")

		st.write("Y finalmente podemos también mostrar la información contenida en formato JSON:")
		st.json({'foo':'bar','fu':'ba'})
		st.code("""st.json({'foo':'bar','fu':'ba'})""")


######################ELEMENTOS GRÁFICOS########################################
	st.header("Elementos gráficos")
	with st.beta_expander("Elementos de Ploteo"):
		st.write("Podemos hacer gráficas lineales (¡y se puede interactuar con ellos!):")
		chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
		st.line_chart(chart_data)
		st.code("""chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.line_chart(chart_data)""")

		st.write("Podemos hacer gráficos de áreas:")
		chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
		st.area_chart(chart_data)
		st.code("""chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.area_chart(chart_data)""")

		st.write(" Podemos hacer gráficos de barras:")
		chart_data = pd.DataFrame(np.random.randn(50, 3),columns=["a", "b", "c"])
		st.bar_chart(chart_data)
		st.code("""chart_data = pd.DataFrame(np.random.randn(50, 3),columns=["a", "b", "c"])
st.bar_chart(chart_data)""")

		st.write("Streamlit además tiene integración con Matplotlib")
		arr = np.random.normal(1, 1, size=100)
		fig, ax = plt.subplots()
		ax.hist(arr, bins=20)
		st.pyplot(fig)
		st.code("""arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)""")

		st.write("También integración con Altair:")
		df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
		c = alt.Chart(df).mark_circle().encode(	x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
		st.altair_chart(c, use_container_width=True)
		st.code("""df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(	x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)""")

		st.write("Y finalmente puede integrarse además con mapas de OpenStreetMaps:")
		df = pd.DataFrame(
		np.random.randn(500, 2) / [50, 50] + [-33.46, -70.65],columns=['lat', 'lon'])#[-33.50, -70.55],columns=['lat', 'lon'])
		st.map(df)

		st.write("De la misma forma anterior, Streamlit puede integrarse con bibliotecas como Vega-Lite, Plotly, Bokeh, PyDeck, DEck_GL y Graphviz. ¡Los invitamos a testearlos! ")
		st.code("""st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)""")

######################ELEMENTOS MULTIMEDIA########################################
	st.header("Elementos Multimedia")
	with st.beta_expander("Elementos de música, audio y video"):
		from PIL import Image
		st.write("En esta sección podemos cargar imágenes directamente desde nuestro PC y agregarle un comentario: ")
		image = Image.open(r'resources/sunrise.jpg')
		st.image(image, caption='Puesto de Sol en las montañas. Ojalá pudiese estar allí. ',use_column_width=True)
		st.code("""image = Image.open('sunrise.jpg')
st.image(image, caption='Puesto de Sol en las montañas. Ojalá pudiese estar allí. ',use_column_width=True)""")

		st.write("Podemos además agregar archivos de audio, como el Valse Opus 64 de Chopin (también conocido como el 'vals del perrito'):")
		audio_file = open(r'resources/Chopin-valse-opus64.ogg', 'rb')
		audio_bytes = audio_file.read()
		st.audio(audio_bytes, format='audio/ogg')
		st.code("""audio_file = open('Chopin-valse-opus64.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')""")

		st.write("""Podemos por otra parte agregar videos directamente desde nuestro PC:""")
		video_file = open(r'resources/Star - 6962.mp4', 'rb')
		video_bytes = video_file.read()
		st.video(video_bytes)
		st.code("""video_file = open('Star - 6962.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)""")

		st.write("Y finalmente también podemos agregar videos de Youtube:")
		st.video('https://www.youtube.com/watch?v=NUYvbT6vTPs') 

######################WIDGETS INTERACTIVOS########################################
	st.header("Widgets Interactivos")
	with st.beta_expander("Widgets"):
		st.write("Dentro de los widgets interactivos podemos incluir botones:")
		if st.button('Digamos hola',key="say_hello"):
		    st.write('Respuesta: ¡Hola quien quiera que seas!')
		else:
			st.write('Respuesta: ¡Adios!')
		st.code("""if st.button('Digamos hola',key="say_hello"):
	st.write('Respuesta: ¡Hola quien quiera que seas!')
else:
	st.write('Respuesta: ¡Adios!')""")

		st.write("Tambien tenemos checkbox para marcar alguna preferancia u opción:")
		agree = st.checkbox('Estoy de acuerdo.')
		if agree:
			st.write('¡Genial! Me acabas de vender tu alma :).')
			st.code("""agree = st.checkbox('Estoy de acuerdo.')
if agree:
	st.write('¡Genial! Me acabas de vender tu alma :).')""")

		st.write("O también radio buttons para marcar entre varias opciones:")
		ingrediente = st.radio("¿Que ingrediente prefieres en la pizza?",('Tocino', 'Piña', 'Choricillo'))
		if ingrediente == 'Tocino':
			st.write('¡Cuidado con el colesterol!.')
		elif ingrediente=='Piña':
			st.write('¡¿En serio?! ¿No me digas que también le echas Coca-Cola al vino?')
		else:
			st.write("Buena elección, padawan.")
		st.code("""ingrediente = st.radio("¿Que ingrediente prefieres en la pizza?",('Tocino', 'Piña', 'Choricillo'))
if ingrediente == 'Tocino':
	st.write('¡Cuidado con el colesterol!.')
elif ingrediente=='Piña':
	st.write('¡¿En serio?! ¿No me digas que también le echas Coca-Cola al vino?')
else:
	st.write("Buena elección, padawan.")""")

		st.write("Las selectboxes te permiten seleccionar una opción dentro de una lista desplegable:")
		opcion = st.selectbox('¿Cómo quieres ser contactado?',('Email', 'Teléfono de casa', 'Celular'))
		st.write('Seleccionaste:', opcion)
		st.code("""	st.write("Las selectboxes te permiten seleccionar más de una opción:")
opcion = st.selectbox('¿Cómo quieres ser contactado?',('Email', 'Teléfono de casa', 'Celular'))
st.write('Seleccionaste:', opcion)""")

		st.write("Existe la opción de elegir múltiples alternativas:")
		opciones= st.multiselect('¿Cuáles son tus colores favoritos?',['Green', 'Yellow', 'Red', 'Blue'],	['Yellow', 'Red'])
		st.write('You selected:', opciones)
		st.code("""	opciones= st.multiselect('¿Cuáles son tus colores favoritos?',['Green', 'Yellow', 'Red', 'Blue'],	['Yellow', 'Red'])
st.write('You selected:', opciones)""")

		st.write("Con el widget 'Slider' puedes elegir un valor,un rango de valores o incluso fechas:")
		x= st.slider("Valor de x:", min_value=1, max_value=100, value=5, step=1, format=None, key=None)
		st.write('Su cuadrado es:', x * x)
		valores = st.slider('Selecciona un rango de valores:',	0.0, 100.0, (25.0, 75.0))
		st.write('Valores:', valores)
		cita = st.slider("Agenda tu cita:",value=(time(11, 00), time(12, 45)))
		st.write("Agendaste tu cita para entre las ", cita[0].strftime("%H:%M")," y las ",cita[1].strftime("%H:%M"))
		st.code("""x= st.slider("Valor de x:", min_value=1, max_value=100, value=5, step=1, format=None, key=None)
st.write('Su cuadrado es:', x * x)
valores = st.slider('Selecciona un rango de valores:',	0.0, 100.0, (25.0, 75.0))
st.write('Valores:', valores)
cita = st.slider("Agenda tu cita:",value=(time(11, 00), time(12, 45)))
st.write("Agendaste tu cita para entre las ", cita[0].strftime("%H:%M")," y las ",cita[1].strftime("%H:%M"))""")

		st.write("Además de lo anterior, podemos también ingresar texto:")
		title_text = st.text_input('Ingresa tu película favorita:', 'Iron Man 3')
		st.write('Tu película favorita es ', title_text)
		st.code("""title_text = st.text_input('Ingresa tu película favorita:', 'Iron Man 3')
st.write('Tu película favorita es ', title_text)""")

		st.write("Podemos insertar números:")
		number = st.number_input('Inserta un número:')
		st.write('Tu número es el ', number)
		st.code("""number = st.number_input('Inserta un número:')
st.write('Tu número es el ', number)""")

		st.write("Podemos agregar tambien en un área de texto para, por ejemplo, analizar sentimientos:")
		txt = st.text_area('Texto a analizar', '''¡Me encanta lo que hace el candidato del partido azul! ¡Vota por el partido azul!''')
		st.write('Sentimiento: ', 'Favorable' )#run_sentiment_analysis(txt))
		st.code("""txt = st.text_area('Texto a analizar', '''¡Me encanta lo que hace el candidato del partido azul! ¡Vota por el partido azul!''')
st.write('Sentimiento: ', 'Favorable' )#run_sentiment_analysis(txt))""")

		st.write("Podemos ingresar fechas u horas:")
		d = st.date_input("¿Cuándo naciste?",date(2019, 7, 6))
		st.write('Naciste el ', d)
		t = st.time_input('Programar alarma para las ', time(8, 45))
		st.write('Alarma programda a las ', t)
		st.code("""d = st.date_input("'¿Cuándo naciste?'",date(2019, 7, 6))
st.write('Naciste el ', d)
t = st.time_input('Programar alarma para las ', time(8, 45))
st.write('Alarma programda a las ', t)""")

		st.write("Finalmente podemos subir un archivo o múltiples archivos:")
		uploaded_file = st.file_uploader("Elige un archivo:")
		if uploaded_file is not None:
		    bytes_data = uploaded_file.read()
		    st.write(bytes_data)
		uploaded_files = st.file_uploader("Elige tus archivos:", accept_multiple_files=True)
		for uploaded_file in uploaded_files:
		    bytes_data = uploaded_file.read()
		    st.write("filename:", uploaded_file.name)
		    st.write(bytes_data)
		st.code("""uploaded_file = st.file_uploader("Elige un archivo:")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
uploaded_files = st.file_uploader("Elige tus archivos:", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)""")
	

######################ELEMENTOS DE PROCESO, INFORMACION Y CONTROL DE FLUJO########################################
	st.header("Procesamiento, Información y Control de Flujo")
	with st.beta_expander("Elementos de Procesamiento:"):
		st.write("Podemos crear elementos que se vayan actualizando con el tiempo:")
		if st.button("Aprietame para iniciar el conteo"):
			with st.empty():
				for seconds in range(3):
					st.write(f"⏳ {seconds} segundos han pasado")
					tim.sleep(1)
				st.write("✔️ conteo de segundos terminado.")
		st.write("Podemos crear una barra de progreso:",key="msje2")
		if st.button("Aprietame para iniciar la barra de carga"):
			my_bar = st.progress(0)
			for percent_complete in range(100):
			    tim.sleep(0.03)
			    my_bar.progress(percent_complete + 1)

		st.write("Podemos también poner elementos de espera:")
		if st.button("Esperar"):
			with st.spinner('Esperando 3 segundos...'):
			    tim.sleep(3)
			st.success('Listo!')
		

	with st.beta_expander("Elementos de información:"):
		st.write("Además podemos crear distintos cuadros para comunicarnos con los usuarios:")
		st.info("Esto es un cuadro de información.")
		st.warning('Esto es un cuadro de advertencia.')
		st.success('Esto es un cuadro de éxito.')
		st.error("Esto es un cuadro de error.")
		e = RuntimeError('También podemos levantar Excepciones. Por ejemplo estos es un RuntimeError')
		st.exception(e)

	with st.beta_expander("Elementos de código:"):
		st.write("Podemos además mostrar código directamente:")
		st.code("""st.write('Este código será impreso en pantalla.')""")

	#######################################################################PLACEHOLDERS, HELPS & OPTIONS


	# placeholder = st.empty()
	# # Replace the placeholder with some text:
	# placeholder.text("Hello")
	# # Replace the text with a chart:
	# placeholder.line_chart({"data": [1, 5, 2, 6]})
	# # Replace the chart with several elements:
	# with placeholder.beta_container():
	#     st.write("This is one element")
	#     st.write("This is another")
	# # Clear all those elements:
	# placeholder.empty()

	# st.help(pd.DataFrame)

	#######################################################################MUTATE DATA
	# df1 = pd.DataFrame(
	#    np.random.randn(50, 20),
	#    columns=('col %d' % i for i in range(20)))
	# # my_table = st.table(df1)
	# df2 = pd.DataFrame(
	#    np.random.randn(50, 20),
	#    columns=('col %d' % i for i in range(20)))
	# # my_table.add_rows(df2)
	# # Now the table shown in the Streamlit app contains the data for
	# # df1 followed by the data for df2.

	# my_chart = st.line_chart(df1)
	# my_chart.add_rows(df2)