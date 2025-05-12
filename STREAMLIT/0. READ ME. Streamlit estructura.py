#ESTRUCTURA STREAMLIT


/mi_proyecto
├─ .streamlit/
│   ├─ config.toml          # Tema, página por defecto, layout, server settings
│   └─ secrets.toml         # Variables sensibles (DB_HOST, DB_USER, DB_PASS, API_KEYS…)
│
├─ assets/                  # Recursos estáticos
│   ├─ images/              # Ilustraciones, logos, fotos de equipo
│   │   ├─ landing_illustration.png
│   │   ├─ data_job_cards_search.png
│   │   └─ …  
│   ├─ icons/               # Iconos personalizados, emojis en SVG/PNG
│   ├─ pdfs/                # CVs, documentación en PDF  
│   └─ styles/              # CSS o snippets de HTML para personalizaciones
│
├─ data/                    # Ficheros CSV, JSON, GeoJSON, etc.
│   ├─ raw/                 # Datos originales (no versionados por Git)
│   │   └─ df_original.csv  
│   ├─ processed/           # Versiones limpias / escaladas  
│   │   └─ df_final.csv  
│   └─ external/            # Descargas externas (Power BI embed, geojson)
│       └─ spain-provinces.geojson  
│
├─ models/                  # Modelos de ML y artefactos serializados
│   ├─ clustering/          # KMeans, DBSCAN, escaladores  
│   │   ├─ kmeans.pkl  
│   │   └─ scaler.pkl  
│   └─ classification/      # Clasificador entrenado  
│       └─ classifier.pkl  
│
├─ notebooks/               # Jupyter notebooks de exploración y prototipado
│   ├─ 01_exploracion.ipynb  
│   ├─ 02_modelado_clustering.ipynb  
│   └─ 03_modelado_clasificacion.ipynb  
│
├─ scripts/                 # Scripts de utilidad (data ingestion, ETL…)
│   ├─ ingest_data.py  
│   └─ generate_geojson.py  
│
├─ src/                     # Código de soporte (módulos de Python reutilizables)
│   ├─ db.py                # Funciones de conexión / consulta a la base de datos  
│   ├─ utils.py             # Helpers comunes (normalización, visualizaciones)  
│   └─ charts.py            # Funciones de trazado para Plotly / Folium  
│
├─ pages/                   # Páginas de Streamlit (ordenadas numéricamente)
│   ├─ 01_Landing.py  
│   ├─ 02_Analisis.py  
│   ├─ 03_Comparativa.py  
│   ├─ 04_SQL_Chart.py  
│   ├─ 05_Clustering.py  
│   ├─ 06_Clasificacion.py  
│   ├─ 07_PowerBI.py  
│   └─ 08_AboutUs.py  
│
├─ tests/                   # Tests unitarios / de integración
│   ├─ test_utils.py  
│   └─ test_db.py  
│
├─ app.py                   # Punto de entrada principal de Streamlit  
├─ requirements.txt         # Dependencias p. ej.  
│   ├─ streamlit>=1.25.0  
│   ├─ pandas  
│   ├─ plotly  
│   ├─ scikit-learn  
│   ├─ mysql-connector-python  
│   └─ …  
├─ .gitignore               # Ignorar /data/raw, /models, /notebooks, secrets.toml, .venv/  
├─ README.md                #  
│   • Descripción del proyecto  
│   • Requisitos y instalación  
│   • Estructura de carpetas  
│   • Uso (comandos para lanzar la app)  
│   • Gestión de secretos  
│   • Contribución / issues  
└─ LICENSE                  # (p. ej. MIT, Apache 2.0)
