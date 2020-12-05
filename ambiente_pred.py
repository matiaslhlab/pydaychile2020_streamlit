import streamlit as st
import comparison_models as md
import pandas as pd
import time
import copy
import SessionState

session_state = SessionState.get(train=False,uploaded_file=None,clean=False, columnas=None,
	df=None, cols_del=None,	y=None, models_selected=None,
	test_size=None, modelos_resul=None, accuracies=None,  
	lista=None,label_model=None)  # Sirve para guardar datos de manera persistente

def write():
	st.caching.clear_cache()
	st.title("Ambiente Predictivo")
	st.header("Detección de cáncer de hígado")
	markdown= """
En este ejemplo vamos a resolver el siguiente problema: necesitamos, a partir de la información de pacientes en India, poder predecir si cierto paciente tiene o no cáncer de hígado. (Este ejemplo fue obtenido en Kaggle del siguiente [link](https://www.kaggle.com/uciml/indian-liver-patient-records)).
Bajo esta premisa, este espacio es un ambiente predictivo donde podremos:
- subir nuestra información
- elegir que variables queremos predecir
- realizar limpieza de la información
- elegir un modelo dentro de una gama de posibilidades
- realizar una comparación entre los modelos
    """
	st.markdown(markdown)
	st.subheader("Finalmente podemos subir un archivo o múltiples archivos:")
	session_state.uploaded_file = st.file_uploader("Elige el archivo de historial de pacientes:",type="csv")
	if session_state.uploaded_file is not None:
		session_state.uploaded_file.seek(0)
		st.write('Dataframe:')
		session_state.df=md.ToDataframe(session_state.uploaded_file)
		st.write(session_state.df)
		session_state.clean = st.checkbox('Limpiar Data de datos nulos.')
		session_state.columnas=tuple(md.GetColumns(session_state.df))
		session_state.cols_del=st.multiselect('¿Qué columnas quieres eliminar?',list(session_state.columnas))		
		session_state.y = st.selectbox('¿Qué variable quieres predecir?',session_state.columnas)
		session_state.models_selected=st.multiselect('¿Qué modelos quieres entrenar?',list(md.GetModelsAvailable()))
		test_size= st.slider("Porcentaje de Testeo:", min_value=10, max_value=90, value=30, step=1, format=None, key=None)/100
		train=st.button('Entrenar modelo/s predictivo/s')
		if train:
			session_state.train=train
			session_state.modelos_resul=[]
			session_state.accuracies=[]
			session_state.lista=[]
			if session_state.clean:
				session_state.df,session_state.label_model=md.CleanData(session_state.df)
			session_state.df=md.DeleteColumns(session_state.df,session_state.cols_del)
			X,Y=md.setX_setY(session_state.df,session_state.y)
			placeholder = st.empty()
			for model in session_state.models_selected:
				placeholder.info("Entrenando modelo: "+model)
				modelo,accuracy=md.TrainModel(model,test_size,X,Y)
				session_state.modelos_resul.append([model,modelo])
				session_state.accuracies.append(accuracy)
				session_state.lista.append([model,accuracy])
				time.sleep(1)
				placeholder.success("Modelo "+model+" listo!")
				time.sleep(1)
		st.dataframe(pd.DataFrame(session_state.lista,columns=[['Modelo','Accuracy']]))
		# st.subheader("Predicción para paciente nuevo:")
		# values=[65,'Female',0.7,0.1,187,16,18,6.8,3.3,0.9]
		# resultados=[]
		# pred=st.button("Predecir")
		# if pred & session_state.train:
			
		# 	values[1]=session_state.label_model.transform([values[1]])[0]
		# 	print(values)
		# 	X_to_pred=pd.DataFrame([values])
		# 	for pair_mod in session_state.modelos_resul:
		# 		if pair_mod[0] in session_state.models_selected:
		# 			resultados.append(md.Predict(pair_mod[1],X_to_pred))
		# 			print(resultados[0])
		# 	st.write(resultados)
		# elif pred & (not session_state.train):
		# 	st.error('Debe entrenar primero algún modelo predictivo.')
		# else: pass
