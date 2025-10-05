import pandas as pd
from src.db_connect import get_engine

def load_web_data(csv_file):
    df = pd.read_csv(csv_file)
    engine = get_engine()
    df.to_sql('web_kpis', engine, if_exists='append', index=False)
    print("✅ Datos web cargados a la base de datos")
