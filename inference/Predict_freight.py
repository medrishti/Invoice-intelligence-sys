import joblib 
import pandas as pd
import os

Model_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'freight-cost-prediction',
    'models',
    'Predicting-Freight-cost.pkl'
)

def load_model(model_path: str = Model_path):
    model = joblib.load(model_path)
    return model

def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    predictions = model.predict(input_df.to_numpy())
    input_df['Predicted_Freight'] = predictions.round()
    return input_df


if __name__ == '__main__':
    sample_data = {
        'Quantity': [10, 5, 2],
        'Dollars': [18500, 9000, 3000],
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)