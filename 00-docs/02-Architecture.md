# Architecture of Oiku

## Backend

### Lenguaje - Python
Python es un lenguaje ampliamente utilizado en el machine learning y analisis de datos. La idea es utilizarlo en mi backend para procesar y organizar los datos, generar predicciones y realizar análisis estadísticos.

### Dependencias

*Se inicia el entorno virtual*
>`python -m venv venv`

*Se instalan con el "requeriments.txt" en la terminal*
>`pip install -r requirements.txt`

#### Backend

- FastAPI
	> Backend
- Uvicorn
	> Servidor Web
- Psycopg
	> Adaptador PostgreSQL
- Sqlalchemy
	> Interactuar con el SQL con POO
- Pydantic
	> Validación de información entre front y back
- Python-dotnenv
	> Leer .env

##### Algoritmos

- Pandas
    > Manipulación masiva de datos

- Numpy
    > Cálculos numéricos y manejo de arrays y matrices.

- Scikit-learn
    > Machine Learning para clasificar datos y detectar anomalías.

- Scipy
    > Cálculos científicos, estadísticos y optimización.

- Joblib
    > Guardar y cargar modelos ya entrenados.

- Statsmodels
    > Modelos estadísticos de series temporales, para la predicción de gastos futuros