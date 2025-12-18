import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Vehículos", layout="wide")

@st.cache_data
def load_data(path="vehicles_us.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as exc:
        st.error(f"No se pudo leer {path}: {exc}")
        return pd.DataFrame()

df = load_data()

st.title("🚗 Dashboard de análisis de vehículos")

if df.empty:
    st.warning("No hay datos cargados. Asegúrate de que 'vehicles_us.csv' esté en la raíz del proyecto.")
    st.stop()

# Mostrar tabla (opcional)
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df.head(200))

st.markdown("---")
st.subheader("Controles para gráficos")

# Columnas numéricas disponibles
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
if not numeric_cols:
    st.error("No hay columnas numéricas en el dataset para graficar.")
    st.stop()

# Checkbox para elegir tipo de gráfico
build_hist = st.checkbox("Construir histograma")
build_scatter = st.checkbox("Construir gráfico de dispersión")
# --- Función utilitaria para preparar DataFrame para graficar ----
def prepare_plot_df(df_in, x_col, y_col, max_sample=5000):
    """
    Devuelve un DataFrame limpio para graficar:
    - Selecciona sólo las columnas x_col y y_col
    - Elimina nulos
    - Recorta percentiles 1% - 99% (para evitar outliers extremos)
    - Si hay más de max_sample filas, realiza un muestreo
    """
    df2 = df_in[[x_col, y_col]].dropna()
    try:
        low_x, high_x = df2[x_col].quantile([0.01, 0.99])
        low_y, high_y = df2[y_col].quantile([0.01, 0.99])
        df2 = df2[
            (df2[x_col] >= low_x) & (df2[x_col] <= high_x) &
            (df2[y_col] >= low_y) & (df2[y_col] <= high_y)
        ]
    except Exception:
        # Si algo falla (p. ej. columnas no numéricas), seguimos sin recorte
        pass

    if len(df2) > max_sample:
        df2 = df2.sample(n=max_sample, random_state=42)

    return df2

# --- Controles de selección (histograma / scatter & columnas) ---
hist_col = st.selectbox("Columna para histograma", options=numeric_cols, index=0)
x_col = st.selectbox("Eje X (scatter)", options=numeric_cols, index=0)
y_col = st.selectbox("Eje Y (scatter)", options=numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

# Casillas para elegir qué gráficos generar
build_hist = st.checkbox("Construir histograma", value=True)
build_scatter = st.checkbox("Construir diagrama de dispersión", value=False)

# Botón para generar
if st.button("Generar gráficos"):
    if build_hist:
        fig = px.histogram(df, x=hist_col, nbins=50, title=f"Histograma de {hist_col}")
        st.plotly_chart(fig, use_container_width=True)

    if build_scatter:
        # Preparar dataframe reducido para graficar (eliminar nulos, recortar outliers y muestrear)
        plot_df = prepare_plot_df(df, x_col, y_col)
    trend_option = "ols"
    if trend_option:
            fig2 = px.scatter(plot_df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}", trendline=trend_option)
        else:
            fig2 = px.scatter(plot_df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")

        st.plotly_chart(fig2, use_container_width=True)

    if not build_hist and not build_scatter:
        st.info("Marca al menos una casilla (histograma o dispersión) antes de hacer clic en 'Generar gráficos'.")
