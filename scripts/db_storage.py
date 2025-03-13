import sqlite3
from sqlalchemy import create_engine

def store_to_db(df, table_name, db_name="data/football_data.db"):

    if df is None or df.empty:
        print(f"No data to store in table '{table_name}'.")
        return
    
    try:
        # Create a connection to SQLite
        engine = create_engine(f"sqlite:///{db_name}")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Data stored in table '{table_name}' successfully")

    except Exception as e:
        print(f"Error storing data: {e}")