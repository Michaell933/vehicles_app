import streamlit as st
import pandas as pd
import plotly.express as px

# --- TÍTULO Y DESCRIPCIÓN ---
st.title('Análisis de Vehículos en EE.UU.')
st.markdown("""
Esta aplicación permite explorar datos sobre vehículos usados listados para la venta en EE.UU.  
Puedes visualizar la distribución de precios, comparar modelos y analizar tendencias.
""")

# --- CARGAR LOS DATOS ---
st.header('1️⃣ Cargar y explorar los datos')

# Ruta del archivo (ajustar si fuera necesario)
DATA_PATH = 'vehicles_us.csv'  # o 'data/vehicles_us.csv' si lo tienes dentro de la carpeta /data

try:
    df = pd.read_csv(DATA_PATH)
    st.success('✅ Datos cargados correctamente.')
    st.write(df.head())
except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {DATA_PATH}. Verifica la ubicación del CSV.")
    st.stop()

# --- DISTRIBUCIÓN DE PRECIOS ---
st.header('2️⃣ Distribución de precios de vehículos')
fig_price = px.histogram(df, x='price', nbins=50, title='Distribución de precios')
st.plotly_chart(fig_price)

# --- FILTRO INTERACTIVO ---
st.header('3️⃣ Distribución de precios por tipo de vehículo')
vehicle_type = st.selectbox('Selecciona el tipo de vehículo:', df['type'].dropna().unique())
filtered_df = df[df['type'] == vehicle_type]
fig_filtered = px.scatter(filtered_df, x='model_year', y='price', color='condition',
                          title=f'Precios por año y condición ({vehicle_type})')
st.plotly_chart(fig_filtered)

# --- CORRELACIÓN ENTRE VARIABLES ---
st.header('4️⃣ Mapa de calor de correlación')
corr = df.select_dtypes(include=['float64', 'int64']).corr()
fig_corr = px.imshow(corr, text_auto=True, title='Correlación entre variables numéricas')
st.plotly_chart(fig_corr)
