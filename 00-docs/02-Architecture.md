# Architecture of Oiku

## Backend

> FastAPI + SQLAlchemy + PostgreSQL

### Structure

```text

app/
├── main.py           # Entry point: creates the FastAPI app and mounts the routers
├── requirements.txt  # Project dependencies
├── core/             # Configuration: environment variables, settings, DB URL
├── db/               # Database connection (Base, engine, session)
├── models/           # SQLAlchemy models (ORM): one class per table
├── schemas/          # Pydantic schemas: validate input/output data
├── routers/          # API endpoints (routes), one per resource
└── services/         # Business logic: queries, analysis, and algorithms

```

### Language - Python

Python is a widely used language in machine learning and data analysis. The idea is to use it in my backend to process and organize data, generate predictions, and perform statistical analysis.

### Dependencies

The virtual environment is created with:-

> `python -m venv venv`

Dependencies are installed from `requirements.txt` in the terminal:-

> `pip install -r requirements.txt`

#### Backend

- FastAPI
  > Backend framework

- Uvicorn
  > Web server

- Psycopg
  > PostgreSQL adapter

- SQLAlchemy
  > Interact with SQL databases using OOP

- Pydantic
  > Data validation between the frontend and backend

- python-dotenv
  > Load `.env` environment variables

##### Algorithms

- Pandas
  > Large-scale data manipulation

- NumPy
  > Numerical computations and array/matrix handling

- Scikit-learn
  > Machine learning for data classification and anomaly detection

- SciPy
  > Scientific and statistical computing and optimization

- Joblib
  > Save and load pre-trained models

- Statsmodels
  > Statistical time-series models for predicting future expenses
