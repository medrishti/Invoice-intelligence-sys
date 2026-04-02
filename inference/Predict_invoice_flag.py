import joblib
import pandas as pd
import os

Model_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'Invoice_flagging',
    'models',
    'predicing_flag_invoice.pkl'
)

def load_model(Model_path:str=Model_path):
    model=joblib.load(Model_path)
    return model

def predict_invoice_flag(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    predictions = model.predict(input_df.to_numpy())
    input_df['Predicted_risk_flag'] = predictions.round()
    return input_df

if __name__ == '__main__':
    sample_data = {
        'invoice_quantity': [10, 5, 2],
        'invoice_dollars': [18500, 9000, 3000],
        'Freight': [500, 200, 100],
        'total_quantity': [100, 50, 20],
        'total_dollars': [185000, 90000, 30000]
    }
    prediction = predict_invoice_flag(sample_data)
    print(prediction)