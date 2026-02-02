# 🚗 Vehicle_Dashboard - Streamlit_App
Dashboard interactivo para explorar datos de vehículos en Estados Unidos. Permite visualizar histogramas, gráficos de dispersión y una línea de tendencia opcional para analizar relaciones entre variables.

📌 Descripción del proyecto

Este proyecto forma parte del Sprint 7 del bootcamp de Data Scientist.
La aplicación permite:

Cargar un dataset de vehículos (vehicles_us.csv)

Elegir columnas numéricas para graficar

Mostrar histogramas personalizables

Generar gráficos de dispersión

Agregar una línea de tendencia (OLS) cuando está disponible

Reducir automáticamente el dataset para mejorar el rendimiento

Todo con una interfaz limpia desarrollada con Streamlit y gráficos de Plotly.

🧠 Tecnologías utilizadas

Python 3.10+

Streamlit

Pandas

Plotly Express


📂 Estructura del repositorio

vehicle_dashboard/

│── app.py

│── requirements.txt

│── vehicles_us.csv

│── README.md   ← este archivo

▶️ Cómo ejecutar la aplicación

1. Clona el repositorio:
```bash
git clone https://github.com/Israelglz15/vehicle_dashboard.git
```

2. Entra a la carpeta:
```bash
cd vehicle_dashboard
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la app:
```bash
python app.py
```

🗂 Dataset utilizado

El archivo vehicles_us.csv contiene información de vehículos usados publicada en anuncios online.

Incluye columnas como:

price

model_year

condition

cylinders

fuel

odometer

transmission

type

paint_color

is_4wd

days_listed


🚀 La app se abrirá en el navegador en:

http://localhost:8501

🌐 Versión desplegada

(agregare esto cuando suba mi app a Render)
🔗 URL de la app: pendiente

👤 Autor

Israel González – Data Scientist en formación.

🎓 Proyecto del Sprint 7 – TripleTen
Statsmodels (opcional para línea de tendencia)
