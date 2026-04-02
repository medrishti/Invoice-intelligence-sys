import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split

def load_vendor_invoice_data(db_path:str):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM vendor_invoice", conn)
    conn.close()
    return df

def prepare_features(df:pd.DataFrame):
    X=df[['Quantity','Dollars']]
    y=df['Freight']
    return X,y

def train_test_split_data(X,y,test_size=0.2,random_state=42):
    return train_test_split(X,y,test_size=test_size,random_state=random_state)
