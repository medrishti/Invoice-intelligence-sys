from model_evaluation_IF import train_random_forest,evaluate_classifier
from data_preprocessing_IF import load_invoice_data,apply_labels,split_data,scale_features
import joblib
import os

FEATURES={
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_quantity",
    "total_dollars"
}

TARGET="flag_invoice"

def main():
    df=load_invoice_data()
    df=apply_labels(df)


    X_train,X_test,y_train,y_test=split_data(df,features=FEATURES,target=TARGET)
    os.makedirs('models', exist_ok=True)
    X_train_scaled,X_test_scaled=scale_features(X_train,X_test,scalar_path='models/scalar.pkl')

    grid_search=train_random_forest(X_train_scaled,y_train)

    evaluate_classifier(grid_search.best_estimator_,
                        X_test_scaled,
                        y_test,
                        'Random Forest Classifier'
                        )

    joblib.dump(grid_search.best_estimator_,'models/predicing_flag_invoice.pkl')


if __name__ == '__main__':
    main()
