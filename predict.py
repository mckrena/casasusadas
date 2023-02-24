import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd

#Definimos función para cargar el modelo
def load_model():
    with open ('saved_steps.pkl', 'rb') as file:
        data = pkl.load(file)
    return data

data = load_model()

tree_loaded = data["model"]
le_comuna = data["le_comuna"]

#En esta función definimos los parámetros que necesitamos rellenar en la app, junto con el diseño de la página
def show_predict():

    st.set_page_config(
        page_title="App Web Precio Viviendas",
        layout="centered",
        page_icon="random")
    
    st.image("header.png")

    #st.title("Predicción del precio de viviendas usadas en Santiago de Chile")

    st.markdown(f'<br><h1 style="color:#a6a6a6;font-size:16px;">{"Complete la siguiente información para realizar la predicción del precio:"}<br><br></h1>', unsafe_allow_html=True)

    comunas = (
        "Calera de Tango",
        "Cerrillos",
        "Cerro Navia",
        "Colina",
        "Conchalí",
        "El Bosque",
        "El Monte",
        "Estación Central",
        "Huechuraba",
        "Independencia",
        "La Cisterna",
        "La Florida",
        "La Granja",
        "La Pintana",
        "La Reina",
        "Lampa",
        "Las Condes",
        "Lo Barnechea",
        "Lo Espejo",
        "Lo Prado",
        "Macul",
        "Maipú",
        "Ñuñoa",
        "Padre Hurtado",
        "Pedro Aguirre Cerda",
        "Peñaflor",
        "Peñalolén",
        "Providencia",
        "Pudahuel",
        "Puente Alto",
        "Quilicura",
        "Quinta Normal",
        "Recoleta",
        "Renca",
        "San Bernardo",
        "San Joaquín",
        "San José de Maipo",
        "San Miguel",
        "San Ramón",
        "Santiago",
        "Vitacura",
    )

    comuna = st.selectbox("Comuna:", comunas)

    habitaciones = st.slider("Número de habitaciones:", 0, 10, 2)

    baños = st.slider("Número de baños:", 0, 10, 2)

    metros = st.number_input("Metros cuadrados construidos:")

    ok = st.button("Calcular Precio")
    if ok:
        X = np.array([[comuna, habitaciones, baños, metros]])
        X[:, 0] = le_comuna.transform(X[:, 0])
        X = X.astype(float)

        precio = tree_loaded.predict(X)
        st.write(f"El precio de vivienda estimado para la comuna de {comuna}, con {habitaciones} habitacion/es, {baños} baño/s y {metros} metros cuadrados construidos, es de ${precio[0]:.0f}.")


    #Otros parámetros de diseño, aquí definimos la fuente a utilizar
    st.write("""
    <style>
    
    @import url('https://fonts.googleapis.com/css2?family=Cinzel&display=swap');html, body, [class*="css"]  {
        font-family: 'Cinzel', serif;
    }
    
    </style>""", unsafe_allow_html=True)

    st.markdown(f'<h1 style="color:#dacb8d;font-size:11px;text-align:center">{"https://github.com/mckrena - http://linkedin.com/in/mckrena"}</h1>', unsafe_allow_html=True)