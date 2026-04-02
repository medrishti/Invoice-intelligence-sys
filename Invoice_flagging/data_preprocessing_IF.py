import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os
def load_invoice_data():
    conn=sqlite3.connect(r"\Users\VBdri\Downloads\inventory.db")

    query=""" 
     WITH purchase_agg AS (
        select p.PONumber,
        count(distinct p.Brand) as total_brands,
        sum(p.Quantity) as total_quantity,
        sum(p.Dollars) as total_dollars, 
        avg(julianday(p.ReceivingDate)-julianday(p.PODate)) as avg_receiving_delay
        from Purchases p
        group by p.PONumber
       )
      SELECT
        vi.Quantity as invoice_quantity,
	    vi.Dollars as invoice_dollars,
	    vi.Freight,
	    (julianday(vi.InvoiceDate) - julianday(vi.PODate)) as days_to_invoice,
	    (julianday(vi.PayDate) - julianday(vi.InvoiceDate)) as days_to_pay,
	    pa.total_brands,
	    pa.total_quantity,
	    pa.total_dollars,
	    pa.avg_receiving_delay
            from vendor_invoice vi
        left join purchase_agg pa
	    on vi.PONumber = pa.PONumber               

     """
    
    df= pd.read_sql_query(query,conn)
    conn.close()
    return df 

def create_invoice_risk_label(row):
     if(abs(row["invoice_dollars"]-row["total_dollars"]) >5):
        return 1
     if(row["avg_receiving_delay"] > 10):
        return 1
    
     return 0

def apply_labels(df):
    df['flag_invoice']=df.apply(create_invoice_risk_label,axis=1)
    return df

def split_data(df,features,target):
    X=df[list(features)]
    y=df[target]

    return train_test_split(X,y,test_size=0.2,random_state=42)

def scale_features(X_train,X_test,scalar_path):
    scalar=StandardScaler()
    X_train_scaled=scalar.fit_transform(X_train)
    X_test_scaled=scalar.transform(X_test)

    os.makedirs(os.path.dirname(scalar_path), exist_ok=True)
    joblib.dump(scalar, scalar_path)
    return X_train_scaled,X_test_scaled





