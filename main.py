from scraper import scrape_data
from db import save_to_database

print("=== Supply Chain Pipeline Starting ===")
df = scrape_data()
save_to_database(df)
print("=== Pipeline Complete ===")