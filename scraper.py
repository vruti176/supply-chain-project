import pandas as pd
from datetime import date
import os

def scrape_data():
    print("Loading data...")
    
    # Download dataset if it doesn't exist
    if not os.path.exists('data/DataCoSupplyChainDataset.csv'):
        os.makedirs('data', exist_ok=True)
        url = "https://raw.githubusercontent.com/vruti176/supply-chain-project/main/data/DataCoSupplyChainDataset.csv"
        df = pd.read_csv(url, encoding='latin-1')
    else:
        df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='latin-1')
    
    df = df[[
        'Category Name',
        'Customer City',
        'Order Region',
        'Sales',
        'Order Item Quantity',
        'Days for shipment (scheduled)',
        'Late_delivery_risk',
        'Order Status'
    ]]
    
    df.columns = [
        'category',
        'city',
        'region',
        'sales',
        'quantity',
        'shipping_days',
        'late_delivery_risk',
        'order_status'
    ]
    
    df['scraped_date'] = str(date.today())
    
    print(f"Loaded {len(df)} rows successfully!")
    return df

if __name__ == "__main__":
    df = scrape_data()
    print(df.head())