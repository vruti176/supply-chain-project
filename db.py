import pandas as pd
import sqlite3

def save_to_database(df):
    print("Saving to local database...")
    
    # Creates a local file called supply_chain.db
    conn = sqlite3.connect('supply_chain.db')
    
    df.to_sql('supply_chain', conn, if_exists='append', index=False)
    
    conn.close()
    print(f"Saved {len(df)} rows to database!")

if __name__ == "__main__":
    from scraper import scrape_data
    df = scrape_data()
    save_to_database(df)