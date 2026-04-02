import sys
sys.path.append('.')
from pathlib import Path
import joblib
from data_preprocessing import load_vendor_invoice_data,prepare_features,train_test_split_data
from model_evaluation import train_LinearRegression,train_decision_tree,train_random_forest,evaluate_model

def main():
    db_path=r'C:\Users\VBdri\Downloads\inventory.db'
    model_dir=Path('models')
    model_dir.mkdir(exist_ok=True)

    df=load_vendor_invoice_data(db_path)
    X,y=prepare_features(df)
    X_train,X_test,y_train,y_test=train_test_split_data(X,y)

    lr=train_LinearRegression(X_train,y_train)
    dt=train_decision_tree(X_train,y_train)
    rf=train_random_forest(X_train,y_train)

    results=[]
    results.append(evaluate_model(lr,X_test,y_test,'Linear Regression'))
    results.append(evaluate_model(dt,X_test,y_test,'Decision Tree'))
    results.append(evaluate_model(rf,X_test,y_test,'Random Forest'))

    best_model_info=min(results,key=lambda x:x['mae'])
    best_model_name=best_model_info['model_name']

    best_model={
        'Linear Regression': lr,
        'Decision Tree': dt,
        'Random Forest': rf
    }[best_model_name]

    model_path= model_dir/'Predicting-Freight-cost.pkl'
    joblib.dump(best_model,model_path)

    print(f'Best model: {best_model_name} with MAE: {best_model_info["mae"]:.2f}')

if __name__=='__main__':
    main()
    


