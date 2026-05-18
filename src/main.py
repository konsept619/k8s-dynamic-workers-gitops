import os
import importlib

def main():

    etl_db_type = os.environ.get("DB_TYPE", "postgres").lower()
    
    try:
        query_module = importlib.import_module(f"queries.{etl_db_type}")
        query_module.run_query()
        
    except ModuleNotFoundError:
        print(f"Error: No module for ETL_TYPE={etl_db_type}")

if __name__ == "__main__":
    main()
