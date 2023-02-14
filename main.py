import streamlit as st
import scraper_ciudad as _scraper1
import scraper_todas_ciudades as _scraper2
import pandas as pd


st.title("Base de datos de los productos de Alpina")
st.write("Consultar productos por ciudades o por todas las ciudades")

opciones = (" ", "Bogotá", "Cali", "Medellín", "Otras Ciudades", "Todas las Ciudades")

opcion_escogida = st.sidebar.selectbox("Seleccione la base de datos deseada", opciones)

if opcion_escogida == "Bogotá":
    st.write("La base de datos de los productos de Bogotá es")
    try:
        datos = _scraper1._ciudad_individual(0)
        st.write(datos)
        df = pd.read_csv("df_BOGOTÁ.csv")
        @st.cache_data 
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)

        st.download_button(
            "DESCARGAR LA BASE DE DATOS",
            csv,
            "file_bogota.csv",
            "text/csv",
            key='download-csv'
            )
    except:
        pass
        
elif opcion_escogida == "Cali":
    st.write("La base de datos de los productos de Cali es")
    try:
        datos = _scraper1._ciudad_individual(1)
        st.write(datos)
        df = pd.read_csv("df_CALI.csv")
        @st.cache_data 
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)

        st.download_button(
            "DESCARGAR LA BASE DE DATOS",
            csv,
            "file_cali.csv",
            "text/csv",
            key='download-csv'
            )
    except:
        pass
elif opcion_escogida == "Medellín":
    st.write("La base de datos de los productos de Medellín es")
    try:
        datos = _scraper1._ciudad_individual(2)
        st.write(datos)
        df = pd.read_csv("df_MEDELLÍN.csv")
        @st.cache_data 
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)

        st.download_button(
            "DESCARGAR LA BASE DE DATOS",
            csv,
            "file_medellin.csv",
            "text/csv",
            key='download-csv'
            )
    except:
        pass
elif opcion_escogida == "Otras Ciudades":
    st.write("La base de datos de los productos de otras ciudades es")
    try:
        datos = _scraper1._ciudad_individual(3)
        st.write(datos)
        df = pd.read_csv("df_OTRAS CIUDADES.csv")
        @st.cache_data 
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)

        st.download_button(
            "DESCARGAR LA BASE DE DATOS",
            csv,
            "file_otras_ciudades.csv",
            "text/csv",
            key='download-csv'
            )
    except:
        pass  
elif opcion_escogida == "Todas las Ciudades":
    st.write("La base de datos de los productos de todas las ciudades es")
    try:
        datos = _scraper2._todas_las_ciudades()
        st.write(datos)
        df = pd.read_csv("todas_las_ciudades.csv")
        @st.cache_data 
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)

        st.download_button(
            "DESCARGAR LA BASE DE DATOS",
            csv,
            "file_todas_las_ciudades.csv",
            "text/csv",
            key='download-csv'
            )
    except:
        pass  





